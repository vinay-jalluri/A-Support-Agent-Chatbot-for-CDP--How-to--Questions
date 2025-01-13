# Support Agent Chatbot for CDPs

![Screenshot (101)](https://github.com/user-attachments/assets/3a43e86e-f8a1-4b41-9187-d8d9af4523e1)

### Objective:
The goal of this project is to develop a chatbot capable of answering "how-to" questions related to four Customer Data Platforms (CDPs): **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot should extract relevant information from the official documentation of these platforms and provide clear, actionable guidance to users.

---

### Data Sources:
The chatbot utilizes the following official documentation for retrieving information:
- **Segment Documentation:** [Segment Docs](https://segment.com/docs/?ref=nav)
- **mParticle Documentation:** [mParticle Docs](https://docs.mparticle.com/)
- **Lytics Documentation:** [Lytics Docs](https://docs.lytics.com/)
- **Zeotap Documentation:** [Zeotap Docs](https://docs.zeotap.com/home/en-us/)

---

### Core Functionalities:

#### 1. Answer "How-to" Questions:
- The chatbot can understand and respond to user questions about performing tasks or using features in the CDPs.
- Example questions:
  - "How do I set up a new source in Segment?"
  - "How can I create a user profile in mParticle?"
  - "How do I build an audience segment in Lytics?"
  - "How can I integrate my data with Zeotap?"

#### 2. Extract Information from Documentation:
- The chatbot retrieves relevant information from the provided documentation.
- It navigates through the content, identifies pertinent sections, and extracts necessary steps or instructions.

#### 3. Handle Variations in Questions:
- Supports varying question lengths, including extremely long or short ones.
- Effectively identifies and handles questions unrelated to CDPs (e.g., "Which movie is releasing this week?").

---

### Bonus Features:

#### 1. Cross-CDP Comparisons:
- The chatbot compares features and processes between the four CDPs.
- Example question: "How does Segment's audience creation process compare to Lytics'?"

#### 2. Advanced "How-to" Questions:
- The chatbot provides guidance on complex or platform-specific tasks, including advanced configurations, integrations, and use cases.

---

### Evaluation Criteria:
- **Accuracy and Completeness:** Ability to provide correct and complete responses.
- **Code Quality and Build:** Clean, modular, and maintainable codebase.
- **Handling Variations:** Effectively manages different phrasings, terminology, and question formats.
- **Bonus Features:** Implementation of cross-CDP comparisons and advanced questions.
- **User Experience:** Smooth and intuitive chatbot interactions.

---

### Implementation Details:
- **Frameworks and Tools:**
  - Natural Language Processing (NLP) libraries or frameworks for text understanding.
  - Alternatively, a simple document indexer for retrieving content.
- **Deployment:** The chatbot can be implemented as a web application using any preferred technology stack.
- **Focus Area:** The emphasis is on **software engineering** rather than model training or building.

---

### Usage:
1. Clone this repository.
2. Set up the environment by installing required dependencies.
3. Launch the chatbot application locally or on a hosting platform.
4. Interact with the chatbot to ask "how-to" questions about Segment, mParticle, Lytics, or Zeotap.

---

### Future Enhancements:
- Add support for more CDPs.
- Enable integration with live chat platforms for real-time assistance.
- Include multilingual support for broader accessibility.

---

### Acknowledgments:
- Special thanks to the creators of Segment, mParticle, Lytics, and Zeotap for their comprehensive documentation.

