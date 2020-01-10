import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good night')
    speak('I am jarvis sir , Please tell me how may I help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please")
        return "none"
    return query


if __name__ == '__main__':
    wishMe()
    if True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak('searching wikipedia....')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query :
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query :
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stackoverflow' in query :
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'play music' in query :
            music_dir = "F:\AUDIO\my fav"
            songs=os.listdir(music_dir)
            print(songs)
            values=random.randrange(0,50,1)
            os.startfile(os.path.join(music_dir,songs[values]))

        elif 'the time' in query :
            strTime= datetime.datetime.now().strftime("%H:%M;%S")
            speak(f" Sir, the time is {strTime}")

        elif 'sublime' in query :
            code_path="E:\\Sublime Text Build 3176 x64\\sublime_text.exe"
            os.startfile(code_path)

        elif 'news' in query :
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()

            soup_page = soup(xml_page, "html.parser")
            news_list = soup_page.findAll("item")
            # Print news title, url and publish date
            for news in news_list:
                print(news.title.text)
                speak(news.title.text)
                print("-" * 60)

        elif 'quit' in query :
            print("Quitting Sir, Thanks for your time..")
            speak("Quitting Sir, Thanks for your time..")
            exit()

