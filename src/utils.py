from random import choice

request_responses = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
    "As you wish, sir.",
    "Ain't nobody got time for that, Except for me sir."
]

morning_greetings = [
    "Good morning sir.",
    "Wake up sir."
]

math_answers = [
    "9 plus 10 equals 19 and 21"
]

def greet():
    print(choice(morning_greetings))