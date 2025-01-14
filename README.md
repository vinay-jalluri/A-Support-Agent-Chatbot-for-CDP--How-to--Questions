# A Support Agent Chatbot for CDP "How-to" Questions

This repository contains the implementation of a Support Agent Chatbot designed to assist users in navigating common "How-to" questions related to a CDP (Customer Data Platform). The chatbot provides relevant, quick, and concise answers, enhancing user experience and operational efficiency.

![Screenshot (101)](https://github.com/user-attachments/assets/1a03c155-fb91-4109-98af-b4bd0c9559d5)

---

## Features
- **User-friendly Interface**: Interacts seamlessly with users to address their queries.
- **Automated Response**: Provides accurate answers to "How-to" questions.
- **Dynamic Learning**: Ability to improve responses by training on new data.
- **Customizable**: Easy to modify for different CDP-related requirements.

---

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: SQL for storing FAQs and training data
- **Libraries**:
  - Natural Language Toolkit (NLTK)
  - TensorFlow/Keras (for machine learning models)
  - Flask for API handling

---

## Project Structure
```
A-Support-Agent-Chatbot-for-CDP--How-to--Questions
|
|-- README.md           # Project documentation
|-- app.py              # Flask application entry point
|-- templates/          # HTML templates
|-- static/             # CSS, JavaScript, and other static files
|-- models/             # Pre-trained machine learning models
|-- data/               # FAQs and training datasets
|-- requirements.txt    # Dependencies
```

---

## Setup Instructions

### Prerequisites
1. Python 3.8 or higher
2. Flask
3. Required Python libraries (listed in `requirements.txt`)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/vinay-jalluri/A-Support-Agent-Chatbot-for-CDP--How-to--Questions.git
   ```
2. Navigate to the project directory:
   ```bash
   cd A-Support-Agent-Chatbot-for-CDP--How-to--Questions
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`.

---

## Usage
1. Open the chatbot in your browser.
2. Enter your "How-to" question in the input field.
3. Receive an accurate and helpful response from the chatbot.
4. If the chatbot cannot answer, it provides an option to log the query for future improvements.

---

## Contribution Guidelines
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request.

---


## Contact
For any queries, feel free to contact the project author:
- **Name**: Jalluri Achutha Sai Vinay
- **GitHub Profile**: [vinay-jalluri](https://github.com/vinay-jalluri)

---

## Future Enhancements
- Integrate voice-based interaction.
- Add multi-language support.
- Improve machine learning models for better accuracy.
- Extend functionality to address broader CDP-related queries.

