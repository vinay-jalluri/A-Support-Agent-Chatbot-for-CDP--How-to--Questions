import requests
from bs4 import BeautifulSoup
import json
import time

CDP_DOC_URLS = {
    "Segment": "https://segment.com/docs/?ref=nav",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_docs():
    data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    session = requests.Session()
    session.headers.update(headers)

    for cdp, url in CDP_DOC_URLS.items():
        try:
            print(f"Scraping {url} for {cdp}")
            response = session.get(url)
            print(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.select('a[href]'):
                    href = link.get('href')
                    if href and not href.startswith('http'):
                        href = url + href

                    try:
                        print(f"Fetching page {href}")
                        page_response = session.get(href, allow_redirects=True)
                        page_response.raise_for_status()
                        page_soup = BeautifulSoup(page_response.text, 'html.parser')

                        content = ' '.join(
                            p.text for p in page_soup.find_all(['p', 'div', 'span', 'code'])
                        )
                        data.append({"platform": cdp, "url": href, "content": content})
                    except Exception as page_error:
                        print(f"Failed to scrape page {href}: {page_error}")

                    time.sleep(1)  # Delay to prevent rate limiting

        except Exception as e:
            print(f"Failed to scrape {cdp}: {e}")

    with open("cdp_docs.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Documentation scraped and saved!")

if __name__ == "__main__":
    scrape_docs()
