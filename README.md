

# Chatbot-Museum

## Overview

Chatbot-Museum is a web-based interactive chatbot designed to assist users with information about a museum. It provides answers to user queries about exhibits, timings, ticketing, and general FAQs using a local knowledge base.

---

## Features

* Interactive chat interface for real-time conversation.
* Local knowledge base stored in a CSV file.
* Fuzzy matching for handling varied user queries.
* Lightweight frontend using HTML, CSS, and JavaScript.
* Backend logic implemented in Python.

---

## Technologies Used

* **Backend:** Python (Flask or similar)
* **Frontend:** HTML, CSS, JavaScript
* **Search:** Fuse.js (fuzzy matching)
* **Data Storage:** CSV file for chatbot responses

---

## Project Structure

```
Chatbot-Museum/
├── app.py                # Backend server for handling queries
├── chatbot_data.csv      # Knowledge base of questions and answers
├── index.html            # Frontend chat interface
├── index.js              # Frontend JavaScript logic
├── styles.css            # Chat UI styling
├── fuse.js               # Fuzzy search library
├── package.json          # Frontend dependencies
└── package-lock.json     # Locked frontend dependencies
```

---

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/karthikeyareddy-7/Chatbot-museum.git
cd Chatbot-museum
```

2. Install Python dependencies (if Flask is used):

```bash
pip install flask pandas
```

3. Run the backend server:

```bash
python app.py
```

4. Open `index.html` in a browser to access the chatbot interface.

---

## Usage

* Type questions related to the museum (e.g., “museum timings”, “ticket prices”, “exhibits information”).
* The chatbot searches the knowledge base and returns the closest matching response.
* Users can continue the conversation in real-time.

---

## Dataset Format

The chatbot uses a CSV file (`chatbot_data.csv`) for its knowledge base:

| Question        | Answer                                             |
| --------------- | -------------------------------------------------- |
| “museum timing” | “The museum is open from 9 AM to 5 PM.”            |
| “ticket price”  | “Ticket costs $10 for adults and $5 for children.” |

Add more questions and answers to expand the chatbot’s knowledge.

---

## Future Enhancements

* Integrate NLP for more flexible responses.
* Add multilingual support.
* Implement speech-to-text and text-to-speech features.
* Connect to a dynamic database for live updates.

---

## Summary

Chatbot-Museum provides an easy-to-use chatbot interface for museum visitors. It demonstrates how a lightweight, web-based chatbot can provide informative responses using a structured knowledge base.

