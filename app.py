from flask import Flask, request, jsonify, render_template, send_from_directory
from indexing import create_index, search_index
import os
import logging
import openai

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# OpenAI API Key (replace this with your actual key)
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key


@app.route("/")
def home():
    """
    Default route to serve the main HTML interface.
    """
    return render_template("index.html")  # Serve the main HTML file


@app.route("/ask", methods=["POST"])
def ask():
    """
    Backend endpoint to process user questions.
    Attempts to retrieve the answer from the index or fallback to OpenAI API.
    """
    # Retrieve the JSON data sent by the frontend
    user_input = request.json.get("question", "").strip()
    platform = request.json.get("platform", "").strip()

    # Input validation
    if not user_input:
        return jsonify({"answer": [{"content": "Please provide a valid question."}]})
    if not platform:
        return jsonify({"answer": [{"content": "Please specify a platform."}]})

    # Step 1: Search the indexed FAQ data
    logging.info(f"Searching for '{user_input}' on platform '{platform}'.")
    response = search_index(platform, user_input)

    if response:  # If results are found in the index
        logging.info(f"Results found in index: {response}")
        return jsonify({"answer": [{"content": result.get("content", "")} for result in response]})

    # Step 2: Fallback to OpenAI API if no results found in the index
    logging.info("No results in the index. Querying OpenAI API.")
    try:
        openai_response = ask_openai(user_input)
        return jsonify({"answer": [{"content": openai_response}]})
    except Exception as e:
        logging.error(f"Error querying OpenAI API: {e}")
        return jsonify({"answer": [{"content": "Sorry, I couldn't process your question. Please try again later."}]})


def ask_openai(question):
    """
    Queries OpenAI's API for an answer if no relevant data is found in the index.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API Error: {e}")
        raise e


if __name__ == "__main__":
    app.run(debug=True)
