# imported libraries and functions
import speech_recognition as sr #*
import pyttsx3 #*
import datetime
import wikipedia #*
import webbrowser
import os
import random
from random import choice
import pyjokes #*
from media import volumeup, volumedown, volumemute, playpause, nexttrack, previoustrack
from utils import requestResponses, morningResponses, mathAnswers

# initialize text-to-speech engine
engine = pyttsx3.init()

# set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate',180)

# function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('[Debug] Listening...\n')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('[Debug] Recognizing...\n')
        query = r.recognize_google(audio, language='en')
        print(f"[Debug] You said: {query}\n")
    except Exception as e:
        print(e)
        speak('Sorry, I did not understand that, could you please repeat it?')
        return "None"
    return query

# function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(choice(morningResponses))
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir,")
    else:
        speak("Good evening sir,")

    speak('''CARLSON is at your service sir.''')

# function to return the weekday name
def weekday():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping = {
        0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"
    }
    try:
        speak(f"Today is {mapping[weekday]}.")
    except:
        pass

# main program loop
if __name__ == "__main__":
    greet()
    while True:
        query = recognize_speech().lower()

        # logic for executing tasks based on query

        if "carlson" in query and "sleep" in query:
            speak("Ok sir, you can call me anytime.")

        ########## CARLSON INTERACTION ##########

        elif "what is your name" in query:
            speak("I am CARLSON, Computer Automated Robotic Listening Software Operations Navigation. How can I be of service sir?")
            continue

        elif "who created you" in query:
            speak("I was created by Collin Laney, on October Thirteenth, Twenty Twenty-Two.")
            continue

        elif "what is your birthday" in query:
            speak("October Thirteenth, Twenty Twenty-Two.")
            continue

        elif "hello" in query:
            speak("Hello sir, how are you?")
            continue

        elif "i am" in query or "i'm" in query:
            speak("That's great sir.")
            continue
            
        elif "how are you" in query:
            speak("Perfect sir.")
            continue
            
        elif "thank you" in query:
            speak("You are welcome sir.")
            continue

        elif "joke" in query:
            speak(pyjokes.get_joke())
            continue

        ########## MEDIA CONTROLS ##########

        elif "resume" in query or "pause" in query:
            playpause()
            continue

        elif "mute" in query:
            volumemute
            continue

        elif "volume up" in query:
            volumeup()
            continue

        elif "volume down" in query:
            volumedown()
            continue

        elif "skip" in query:
            nexttrack()
            continue

        elif "previous" in query:
            previoustrack()
            continue

        ########## SYSTEM APPLICATIONS ##########


        ########## CARLSON REQUESTS ##########

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening YouTube...')
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open('https://www.google.com/')

        elif 'play music' in query:
            music_dir = 'PATH_TO_YOUR_MUSIC_DIRECTORY'
            songs = os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'stop' in query or 'bye' in query or 'goodbye' in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I am not able to do that right now. Please try again later.")

