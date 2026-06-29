"Jarvis 1.0"

#will import the required modules

import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
import music
import requests


recognizer = sr.Recognizer()   #recognizer is the class helps in take the speech recognizer funtionallity
engine = pyttsx3.init()        # initialize the engine also seen from pyttsx3 website


#Here we will define the function which will help in speaking the text given to it.
def speak(text):
    print("jarvis Speaking:", text)
    engine.say(text)
    engine.runAndWait()

#Here we will define the function which will help in processing the command given to it.
def processCommand(c):
#will open following site.
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("http://whatsapp.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif c.lower().startswith("play"):  #tricky code but understable
        song = c.lower().split(" ")[1]
        link = music.musics[song]
        webbrowser.open(link)
#will tell news with the help of newsdata.io api
    elif "news" in c.lower():  #with the help of ai
        # print("Fectching news....")  #testing
        url = "https://newsdata.io/api/1/latest?YOUR_API_KEY=in&language=en"
        response = requests.get(url)
        data = response.json()
        articles = data["results"]
        speak("here are todays top news")
        for article in articles:
            speak(article["title"])

#The program will continue if the  __name__ is "__main__" which means the program is being run directly and not imported as a module.
if __name__ == "__main__" :
    speak("Initializing jarviss..... ")
    while True:
        # wake up only when we call jarvis..

        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing....")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source , timeout= 2 , phrase_time_limit= 1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("yes sir")
                # this will listen and response
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source , timeout= 4 , phrase_time_limit= 4)
                    command = r.recognize_google(audio)

                processCommand(command)
        except Exception as e:  #THis will catch the exception if any error occurs in the try block and print the error message.
            print("Error; {0}".format(e))
