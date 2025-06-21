#  Chatbot using NLP | CodTech Internship - Task 03

This project is part of the CodTech Python internship. The goal is to build a chatbot using **Natural Language Processing (NLP)** techniques with **NLTK**, capable of responding to user queries through pattern matching and simple logic.

---

##  Task Description

> **Task 03 – AI Chatbot with NLP**  
> Build a chatbot using NLP libraries like NLTK or spaCy, capable of answering user queries.

---

##  Project Features

- Rule-based conversation system
- Uses `nltk.chat.util.Chat` and `reflections` to simulate interaction
- Handles common greetings, questions, and exit commands
- Easily extendable with more custom responses

---

## File Structure

<pre>TASK03_CODTECH/
├── chatbot.py # Main chatbot script
├── setup_nltk.py # NLTK data downloader
├── requirements.txt # List of dependencies
└── README.md # Project documentation </pre>

---

##  Requirements

Install dependencies using pip:

pip install nltk

Then run the NLTK setup script to download required datasets:

python setup_nltk.py

---
### How to Run

### 1. Open your terminal in the project folder.

### 2. Start the chatbot by running:

python chatbot.py

### 3.Example conversation:

Hi! I'm your CodTech chatbot. Type 'exit' to end.

You: hello
Bot: Hello!

You: what is your name?
Bot: I am a chatbot created for CodTech Internship Task 03.

You: bye
Bot: Goodbye!

---

### Features

1. Rule-based responses using regular expressions

2. Uses nltk.chat.util.Chat and reflections to mimic human conversation

3. Easily extendable with more patterns and responses

---

### Submitted by Vikas V

