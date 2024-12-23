import pyttsx3 as tts
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import pyjokes
import pywhatkit as kit
import pyautogui as pg
import numpy as np
import subprocess




def start():
    engine = tts.init()
    rate= engine.getProperty('rate')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    engine.say("Hello, I am Friday your personal assistant")
    engine.runAndWait()
    while True:
        query = input("You: ")
        if "hi" in query.lower() or "hello" in query.lower():
            engine.say("How can I help you?")
            engine.runAndWait()
        
        elif "joke" in query.lower():
            jokes = pyjokes.get_joke() 
            print(jokes) 
            engine.say(jokes) 
            engine.runAndWait()
        
        elif "date" in query.lower():
            today = datetime.date.today()
            date_string = today.strftime("%B %d, %Y")
            print(date_string)
            engine.say(f"The date is {date_string}")
            engine.runAndWait()
        
        elif "time" in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            engine.say(f"The time is {time}")
            engine.runAndWait()
            
        elif "wikipedia" in query.lower():
            query = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result) 
                engine.say(result)
                engine.runAndWait()
            except wikipedia.exceptions.PageError:
                print(f"No Wikipedia page found for '{query}'")
        
        elif "open google" in query.lower():
            os.system("start Chrome")
            engine.say("Opening Google")
            engine.runAndWait()
        
        elif "open brave" in query.lower():
            os.system("start Brave")
            engine.say("Opening Brave")
            engine.runAndWait()
        
        elif "open youtube" in query.lower():
            webbrowser.open("https://www.youtube.com")
            engine.say("Opening Youtube")
            engine.runAndWait()
        
        elif "open stackoverflow" in query.lower():
            webbrowser.open("https://www.stackoverflow.com")
            engine.say("Opening stackoverflow")
            engine.runAndWait()
            
        
        elif "play" in query.lower():
            query = query.replace("play", "").strip()
            kit.playonyt(query)
            engine.say(f"Playing {query} on YouTube")
            engine.runAndWait()
        
        elif "open snap" in query.lower():
            webbrowser.open("https://www.snapchat.com")
            engine.say("Opening Snapchat")       
            engine.runAndWait()
        
        elif "open insta" in query.lower():
            webbrowser.open_new("https://www.instagram.com")
            engine.say("Opening Instagram")
            engine.runAndWait()
        
        elif "open discord" in query.lower():
            webbrowser.open("https://www.discord.com")
            engine.say("Opening Discord")
            engine.runAndWait()
        
        elif "open zoom" in query.lower():
            webbrowser.open("https://www.zoom.us")
            engine.say("Opening Zoom")
            engine.runAndWait()
        
        elif "open meet" in query.lower():
            webbrowser.open("https://www.meet.google.com")
            engine.say("Opening Google Meet")
            engine.runAndWait()
        
        elif "open teams" in query.lower():
            webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/microsoft-teams/group-chat-software")
            engine.say("Opening Microsoft Teams")
            engine.runAndWait()
        
        elif "open whatsapp" in query.lower():
            try:
                subprocess.run(["powershell", "-Command", "Start-Process -FilePath 'whatsapp:'"], check=True)
                engine.say("Opening Whatsapp Desktop")
                engine.runAndWait()
                continue
                return True
            except subprocess.CalledProcessError as e:
                print(f"Error launching WhatsApp Desktop: {e}")
                return False
            continue
        
        elif "open mail" in query.lower():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            engine.say("Opening Gamail")
            engine.runAndWait()
            
        elif "mssg" in query.lower():
            query = query.replace("mssg", "").strip()
            kit.sendwhatmsg("+910000000000", "Hello i am friday", 15, 3, )
            time.sleep(10)
            engine.say(f"Message sent to {query}")
            engine.runAndWait()
        
        elif "calculate" in query.lower():
            query = query.replace("calculate", "").strip()
            result = eval(query)
            print(result)
            engine.say(f"The result of {query} is {result}")
            engine.runAndWait()
        
        elif "search" in query.lower():
            query = query.replace("search", "").strip()
            kit.search(query)
            engine.say(f"Searching for {query}")
            engine.runAndWait() 

        elif "thank you" in query.lower():
            engine.say("You are welcome")
            engine.say("I am always here to help you")
            engine.runAndWait()
        
        elif "exit" in query.lower() or "bye" in query.lower():
            engine.say("Goodbye")
            engine.runAndWait()
            os.system("taskkill /f /im Code.exe") 
            break
        else:
            engine.say("I am sorry, I did not understand")
            engine.runAndWait()
            continue

if __name__ == "__main__":
    start()

