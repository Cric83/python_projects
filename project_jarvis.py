import pyttsx3  # pip install pyttsx3
import wikipedia   # pip install wikipedia
import datetime
import speech_recognition as sr   # pip install speechRecognition
import webbrowser   
import smtplib


engine = pyttsx3.init('sapi5')   # sapi5 is used to take voices from windows inbuild
voices = engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)  # voices[0].id gives voice of male and voice[1].id will give voice of female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    
    else:
        speak("Good Night sir")

    speak("I am Jarvis sir, Please tell me how can I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening.....")
       r.pause_threshold=1   # minimum seconds to which jarvis hears
       audio=r.listen(source)

    try:
      print("Recognising...")
      query=r.recognize_google(audio, language='en-in')
      print(f"user said:{query}\n")
    except Exception as e:
      #print(e)
      print("say that again please...")
      return "None"
    return query

def sendEmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", 'your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


    
if __name__  == "__main__":
    wishme()
    while True:
         
        query =takeCommand().lower()
# logic for executing tasks

if 'wikipedia' in query:
    speak("searching  wikipedia...")
    query=query.replace("wikipedia",'')
    results=wikipedia.summary(query,sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

elif 'open youtube' in query:   # to search youtube
    webbrowser.open("youtube.com")

elif 'open google' in query:   # to search google
    webbrowser.open('google.com')

elif 'open stackoverflow' in query:   # to search stackoverflow
    webbrowser.open('stackoverflow.com')

elif 'play music' in query:     # to play music
    music_dir='F:\\Audio Songs'
    songs=os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[0]))

elif 'the time' in query:     # to get time
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"SIR the time is {strTime}")

elif 'open notepad' in query:   # to open notepad ++
    codepath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
    os.startfile(codepath)

elif 'send email' in query:   # to send e-mail
    try:
        speak("what should i say?")
        content=takeCommand()
        speak("to whom you want to send mail")
    except Exception as e:
        print(e)
        speak("sorry e-mail sending failed")

elif 'quit' in query:
    exit()

 