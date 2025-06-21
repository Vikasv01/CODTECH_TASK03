import nltk
from nltk.chat.util import Chat, reflections

# Define pairs: (input, response)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created for CodTech Internship Task 03."]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of Python code, but I'm doing fine!"]
    ],
    [
        r"bye|exit",
        ["Goodbye!", "See you later!", "Bye! Take care."]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Could you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm your CodTech chatbot. Type 'exit' to end.\n")
chatbot.converse()
