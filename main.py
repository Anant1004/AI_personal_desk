import win32com.client
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.speak(text)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning Sir!")
    elif(hour>=12 and hour <18):
        speak("Good afternoon Sir !")
    else:
        speak("Good Evening Sir !")
    speak("Hi I am Alex, please command me !")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recongning.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        # print(e)
        print("Can you say that again !!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('twinkle127k@gmail.com','')
    server.sendmail('twinkle127k@gmail.com',to, content)
    server.close() 

if __name__ =='__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube Sir!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google Sir!")
            webbrowser.open("Google.com")

        elif 'open instagram' in query:
            speak("Opening Instagram Sir!")
            webbrowser.open("instagram.com")


        elif 'play music' in query:
            music_dir = "D:\\musics"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, The Time is {strtime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\anant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'email to ak' in query:
            try:
                speak("What should I say ? ")
                content = takeCommand()
                to = "twinkle127k@gmail.com"
                sendEmail(to,content)
                speak("Email, sent!")
                print("Email sent!")
            except Exception as e:
                print(e)
                speak("Some error occured while sending please try to re-send again")