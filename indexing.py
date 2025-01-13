import os
import json
import logging
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

# Setup logging
logging.basicConfig(level=logging.INFO)


def create_index():
    """
    Create or rebuild the Whoosh index from `cdp_docs.json` data.
    """
    # Load JSON data
    with open("cdp_docs.json", "r") as f:
        data = json.load(f)

    # Prepare index directory
    index_dir = "indexdir"
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    # Define schema: platform, URL, content (combined question & answer)
    schema = Schema(
        platform=TEXT(stored=True),
        url=TEXT(stored=True),
        content=TEXT(stored=True)  # Combined "question + answer"
    )

    # Create or open an existing index
    ix = create_in(index_dir, schema)
    writer = ix.writer()

    # Add data to the index
    for entry in data:
        platform = entry["platform"]
        url = entry["url"]
        for faq in entry["content"]:
            question = faq.get("question", "").strip()
            answer = faq.get("answer", "").strip()

            # Combine question and answer for better search matching
            full_content = f"{question} {answer}".lower()  # Normalize text

            writer.add_document(platform=platform, url=url, content=full_content)

    writer.commit()
    logging.info("Index successfully created.")


def search_index(platform, search_query):
    """
    Searches the index for matching documents based on platform and query.
    Filters results by the platform name.
    """
    index_dir = os.path.join(os.getcwd(), "indexdir")
    if not os.path.exists(index_dir):
        logging.error("Index directory does not exist. Please run create_index().")
        return []

    try:
        ix = open_dir(index_dir)
        with ix.searcher() as searcher:
            # Parse the content field to find matches
            query_parser = QueryParser("content", schema=ix.schema)
            parsed_query = query_parser.parse(search_query.lower())  # Normalize to lowercase
            results = searcher.search(parsed_query, limit=5)

            # Debug logs
            logging.info(f"Search query: {search_query}")
            logging.info(f"Raw search results: {[dict(hit) for hit in results]}")

            # Filter by platform
            filtered_results = [
                dict(result) for result in results if result.get("platform") == platform
            ]
            logging.info(f"Filtered results for platform '{platform}': {filtered_results}")
            return filtered_results
    except Exception as e:
        logging.error(f"Error occurred during search: {e}")
        return []
