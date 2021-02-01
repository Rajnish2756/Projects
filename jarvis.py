from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import wolframalpha
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import base64



class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=600, height=600)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(Image.open('Peter.gif'))]
        self.image = self.canvas.create_image(300,300, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'name':'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()
window.configure(bg="Black")

global var
global var1

var = StringVar()
var1 = StringVar()

password="Senders Email Password"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akshaychaturvedi544@gmail.com', password) # email id - use any email id whose security/privacy is off
    server.sendmail('akshaychaturvedi544@gmail.com', to, content)
    server.close()
    
username="Sir!"
ainame="Jarvis 1.o"
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set(f"Good Morning {username}") #Name - your Name
        window.update()
        speak(f"Good Morning {username}")
    elif hour >= 12 and hour <= 18:
        var.set(f"Good afternoon {username}")
        window.update()
        speak(f"Good afternoon {username}")
    else:
        var.set(f"Good evening {username}")
        window.update()
        speak(f"Good evening {username}")
    speak(f"Myself {ainame} How may I help you sir") #BotName - Give a name to your assistant

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        var.set(f"{username}, Can you repeat the command please?")
        window.update()
        speak(f"{username}, Can you repeat the command please?")
        return "None"
    
    var1.set(query)
    window.update()
    return query

def takeEmail():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        var.set(f"{username}, Can you repeat the command please?")
        window.update()
        speak(f"{username}, Can you repeat the command please?")
        return "None"
    
    var1.set(query)
    window.update()
    return query.replace(" ","")

count=0

def play():
    global count
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    if count==0:
        wishme()
    count=1
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'thank you' in query:
            var.set(f"It was Pleasure Helping You {username}")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak(f"It was Pleasure Helping You {username}")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set(f"sorry {username}, could not find any result")
                    window.update()
                    speak(f"sorry {username}, could not find any result")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'open course era' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
			
        elif 'open stack overflow' in query:
            var.set('opening stack overflow')
            window.update()
            speak('opening stack overflow')
            webbrowser.open('stackoverflow.com')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            os.startfile("C:\\Users\Rajnish Chanchal\Desktop\Amazon Music.lnk")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break 

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" %strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am mature enough to help you sir")
            window.update()
            speak("I am mature enough to help you sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player.lnk" #Enter the correct Path according to your system
            os.startfile(path)
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'your name' in query:
            var.set(f"Myself {ainame} Sir")
            window.update()
            speak(f'myself {ainame} sir')

        elif 'who creates you' in query:
            var.set('My Creator is Shivanshu and Rajnish')
            window.update()
            speak('My Creator is Shivanshu and Rajnish')

        elif 'say hello' in query:
            var.set(f'Hello Everyone! My self {ainame}')
            window.update()
            speak(f'Hello Everyone! My self {ainame}')

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk" #Enter the correct Path according to your system
            os.startfile(path)
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'send email' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                var.set('please give me reciever email id')
                window.update()
                speak('please give me reciever email id')
                
                to = takeEmail()
                
                var.set(f"sending email to {to}")
                window.update()
                var.set(f'confirm send email to {to}')
                window.update()
                speak(f'confirm send email to {to}')
                confirm=takeCommand()
                if 'yes' in confirm:
                    sendemail(to, content)
                    var.set('Email has been sent!')
                    window.update()
                    speak('Email has been sent!')
                elif 'no' in confirm:
                    var.set('email sending cancelled')
                    window.update()
                    speak('email sending cancelled')
                
            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
		
        elif "open python" in query:
            var.set("Opening Python Idle")
            window.update()
            speak('opening python Idle')
            os.startfile('C:\\Users\Rajnish Chanchal\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\IDLE (Python 3.8 64-bit)') #Enter the correct Path according to your system
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
        
        elif "write a note" in query:
            var.set('What should i write,sir')
            window.update()
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            var.set('Sir, should i include date and time')
            window.update()
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                var.set('done sir')
                window.update()
                speak('done sir')
            else:
                file.write(note)
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
                
        elif "show notes" in query:
            var.set('Showing Notes')
            window.update()
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            file.read()
            var.set(f'{file.read(6)}')
            window.update()
            speak(file.read(6))
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif "calculate" in query: 
             
            try:
                app_id = "V7KLV6-Y5GQ54UQR7"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate') 
                query = query.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text
                var.set(f"The answer is {answer}")
                window.update()
                speak(f"The answer is {answer}")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
            except:
                var.set("No result")
                window.update()
                speak("No result")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
        
        elif "what is" in query or "who is" in query:
            app_id = "V7KLV6-Y5GQ54UQR7"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
             
            try:
                var.set(f"{next(res.results).text}")
                window.update()
                speak(f"{next(res.results).text}")
            except StopIteration:
                var.set("No results")
                window.update()
                speak("No result")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break


label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

window.title('JARVIS')

app=App(window)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()


