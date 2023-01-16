import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import streamlit as st


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognising...")
        Query = r.recognize_google(audio,language='en-in')
        print(f"User said: {Query}")
        speak(Query)
    except Exception as e:
        speak("Say that again please....")
        return "None"
    return Query
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 17:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hi sir!,I am jarvis sir.how can i help you")


st.title("Financial Queries")

while True:
    wish()
    speak("please tell sir!,what I need to search in wikipedia.....")
    query = st.text_input("Enter the Query: ")
    results = wikipedia.summary(query, sentences=2)
    if st.button("Search"):
        speak("According to Wikipedia")
        st.write(results)
        speak(results)








