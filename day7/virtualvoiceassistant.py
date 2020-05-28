import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import datetime
import random
import wikipedia
import webbrowser
import smtplib

def speak(text):
    i = random.randint(0,10)
    eng = text
    obj = gTTS(text =  eng , lang ='en')
    obj.save(f'audio{i}.mp3') #save the file in working directory in mp3 file format
    playsound(f'audio{i}.mp3')  #we pass the path in this
    os.remove(f'audio{i}.mp3')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning sam Sir \n !.I am JARVIS.Please tell me how may I help you")
    elif hour >= 12 and hour <17:
        speak("Good Afternoon sam Sir!.I am JARVIS.Please tell me how may I help you")
    else:
        speak("Good Evening sam Sir!.I am JARVIS.Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        try:
            output = r.recognize_google(audio)
            print("You said :{}".format(output))
            return output
        except:
            print("I didnt recognize")
            return "I didnt recognize"

def sendEmail(to,msg):
    server = smtplib.SMTP('smatp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your id','password')
    server.sendmail('your id',to,msg)
    server.close()

if __name__ == "__main__":
    wishMe()
    print("To exit say exit.")
    print("Give Command")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching wikipedia....")
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =4)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query or 'date' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            date = datetime.date.today()
            print(date)
            print(strTime)
            speak(f"Sir the time is {strTime} and the date is {date}")
        elif 'open code' in query:
            path = "C:\\Users\\SHAKSHAM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'music' in query:
            songsList = "path"
            songs= os.listdir(songsList)
            print(songsList)
            os.startfile(os.path.join(songsList,songs[random.randint(0,100)]))
        elif 'email' in query:
            try:
                print("What you want to send")
                speak("What you want to send")
                msg = takeCommand()
                to = "sshaksham31@gmail.com"
                sendEmail(to,msg)
                print("Email has been sent")
                speak("Email has been sent")
            except:
                print("Unable to send")
                speak("Unable to send")
        elif 'restart' in query:
            os.system("shutdown /r")
        elif 'shutdown' in query:
            os.system("shutdown /s")
        elif 'exit' in query:
            break
        else:
            print("Invalid Command..")
        print("Give Next Command:")
