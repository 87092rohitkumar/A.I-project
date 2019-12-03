
import json
import requests
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time
import playsound
from playsound import playsound
from gtts import gTTS

engine = pyttsx3.init('sapi5')
URL = 'https://www.way2sms.com/api/v1/sendCampaign'

client = wolframalpha.Client('ur api')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning take breakfast !')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon take lunch!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening take snacks!')


wishme()
speak('How may I help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("Recognizing...")
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query
def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=932ddd38d3ff4abc99237b63805c86e9"
    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()
    # getting all articles in a string article
    article = open_bbc_page["articles"]
    # empty list which will
    # contain all trending news
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohitkrltr121@gmail.com', 'ur apssword')
    server.sendmail('rohitltr121@gmail.com', to, content)
    server.close()

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
     'senderid':senderId
  }
  return requests.post(reqUrl, req_params, phoneNo)
if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open news'in query:
            speak('okay')
            webbrowser.open('www.timesofindia.indiatimes.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif "who are you" in query or "define yourself" in query:
            speak('okay')
            speak('''Hello, I am your personal lady Assistant.
            I am here to make your life easier. You can pass the command me to perform 
            various tasks such as mathematical probelam and general knowledge question and also anicent things or opening applications excectra''')
        elif "who made you" in query or "who created you" in query:
            speak ('I have been created by Rohit  Kumar')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'open bing' in query:
            speak('okay')
            webbrowser.open('www.bing.com')
        elif 'open yahoo' in query:
            speak('okay')
            webbrowser.open('www.yahoo.com')
        elif 'open firefox' in query:
            speak('okay')
            webbrowser.open('www.firefox.com')
        elif 'open stackoverflow' in query:
            speak('okay')
            webbrowser.open('www.stackoverflow.com')
        elif 'open geeksforgeeks' in query:
            speak('okay')
            webbrowser.open('www.geeksforgeeks.com')
        elif 'open edureka' in query:
            speak('okay')
            webbrowser.open('www.edureka.com')
        elif 'open Tutorialspoint' in query:
            speak('okay')
            webbrowser.open('www.Tutorialspoint.com')

        elif 'open coursera' in query:
            speak('okay')
            webbrowser.open('www.coursera.com')
        elif 'Week _name' in query:
            speak('okay')
            week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(week)
        elif 'current_year' in query:
            speak('okay')
            today = str(datetime.date.today());
            curr_year = int(today[:4]);
            curr_month = int(today[5:7]);
            print(today)

        elif 'today' in query:
            now = datetime.datetime.now()
            print(now.strftime("%A"))
        elif 'currentDate' in query:
            Current_Date = datetime.datetime.today()
            print(str(Current_Date))
        elif 'time' in query:
            speak('okay')
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif "how was the day" in query:
            stMsgs = ['good!', 'awesome', 'Nice!', 'bad','not good as last day',]
            speak(random.choice(stMsgs))
        elif "open News" in query:
            speak('okay')
            webbrowser.open("https://indianexpress.com/")
        elif "play news" in query:
            speak('okay')
            NewsFromBBC()
        elif 'send message' in query:
            try:
                speak("What u want send?")
                #content = myCommand()
                content = myCommand()
                response = sendPostRequest(URL, '4X5G25S9H1CU4V0STO04Q5HGZCJZXLD4', 'KWJMATK6EVF04WJO', 'stage','ur mobile number', 'ur email id', 'good afternoon rohit take lunch')
                speak("message has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend rohit. I am not able to send this message")
        elif 'send mail' in query:
            try:
                speak("What u want send?")
                content = myCommand()
                to = "2nd email id"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend rohit. I am not able to send this email")

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'play music' in query:
             music_folder ='D:\\myfav\\'
             music = ['bhola_bhandari','sun_rha_hai','mere_papa','T', 'kaun_tujhe','Teri_Masumiyat','Zindagi_Mein_Koi']
             random_music = music_folder + random.choice(music) + '.mp3'
             os.system(random_music)
             speak('Okay, here is your music! Enjoy!')
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('According to your search - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=1)
                    speak('Got it.')
                    speak('wikipedia search :- ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
