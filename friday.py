# Import required libraries
import pyttsx3 as tts          # Text-to-speech conversion library
import datetime                # For date and time operations
import wikipedia              # For fetching Wikipedia information
import webbrowser             # For opening websites
import os                     # For system operations
import random                 # For random operations
import time                   # For time-related operations
import pyjokes                # For generating random jokes
import pywhatkit as kit      # For YouTube and WhatsApp operations
import pyautogui as pg       # For GUI automation
import numpy as np           # For numerical operations
import subprocess            # For running system commands

def start():
    # Initialize text-to-speech engine
    engine = tts.init()
    
    # Configure speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # Sets speed of speech
    
    # Configure voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Sets default voice
    
    # Greet the user
    greet=  '''
                    ███████╗██████╗ ██╗██████╗  █████╗ ██╗   ██╗
                    ██╔════╝██╔══██╗██║██╔══██╗██╔══██╗╚██╗ ██╔╝
                    █████╗  ██████╔╝██║██║  ██║███████║ ╚████╔╝ 
                    ██╔══╝  ██╔══██╗██║██║  ██║██╔══██║  ╚██╔╝  
                    ██║     ██║  ██║██║██████╔╝██║  ██║   ██║   
                    ╚═╝     ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝
            '''
    print(greet)
    
    # Initial greeting
    engine.say("Hello, I am Friday your personal assistant")
    engine.runAndWait()
    
    # Main loop for continuous interaction
    while True:
        # Get user input
        query = input("You: ")
        
        # Basic greeting responses
        if "hi" in query.lower() or "hello" in query.lower():
            engine.say("How can I help you?")
            engine.runAndWait()
        
        # Joke feature
        elif "joke" in query.lower():
            jokes = pyjokes.get_joke()
            print(jokes)
            engine.say(jokes)
            engine.runAndWait()
        
        # Date information
        elif "date" in query.lower():
            today = datetime.date.today()
            date_string = today.strftime("%B %d, %Y")
            print(date_string)
            engine.say(f"The date is {date_string}")
            engine.runAndWait()
        
        # Time information
        elif "time" in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            engine.say(f"The time is {time}")
            engine.runAndWait()
        
        # Wikipedia search
        elif "wikipedia" in query.lower():
            query = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                engine.say(result)
                engine.runAndWait()
            except wikipedia.exceptions.PageError:
                print(f"No Wikipedia page found for '{query}'")
        
        # Browser operations - Google Chrome
        elif "open google" in query.lower():
            os.system("start Chrome")
            engine.say("Opening Google")
            engine.runAndWait()
        
        # Browser operations - Brave
        elif "open brave" in query.lower():
            os.system("start Brave")
            engine.say("Opening Brave")
            engine.runAndWait()
        
        # Website operations - YouTube
        elif "open youtube" in query.lower():
            webbrowser.open("https://www.youtube.com")
            engine.say("Opening Youtube")
            engine.runAndWait()
        
        # Website operations - Stack Overflow
        elif "open stackoverflow" in query.lower():
            webbrowser.open("https://www.stackoverflow.com")
            engine.say("Opening stackoverflow")
            engine.runAndWait()
        
        # YouTube video playback
        elif "play" in query.lower():
            query = query.replace("play", "").strip()
            kit.playonyt(query)
            engine.say(f"Playing {query} on YouTube")
            engine.runAndWait()
        
        # Social media - Snapchat
        elif "open snap" in query.lower():
            webbrowser.open("https://www.snapchat.com")
            engine.say("Opening Snapchat")
            engine.runAndWait()
        
        # Social media - Instagram
        elif "open insta" in query.lower():
            webbrowser.open_new("https://www.instagram.com")
            engine.say("Opening Instagram")
            engine.runAndWait()
        
        # Communication platform - Discord
        elif "open discord" in query.lower():
            webbrowser.open("https://www.discord.com")
            engine.say("Opening Discord")
            engine.runAndWait()
        
        # Video conferencing - Zoom
        elif "open zoom" in query.lower():
            webbrowser.open("https://www.zoom.us")
            engine.say("Opening Zoom")
            engine.runAndWait()
        
        # Video conferencing - Google Meet
        elif "open meet" in query.lower():
            webbrowser.open("https://www.meet.google.com")
            engine.say("Opening Google Meet")
            engine.runAndWait()
        
        # Communication platform - Microsoft Teams
        elif "open teams" in query.lower():
            webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/microsoft-teams/group-chat-software")
            engine.say("Opening Microsoft Teams")
            engine.runAndWait()
        
        # Messaging - WhatsApp Desktop
        elif "open whatsapp" in query.lower():
            try:
                # Launch WhatsApp using PowerShell command
                subprocess.run(["powershell", "-Command", "Start-Process -FilePath 'whatsapp:'"], check=True)
                engine.say("Opening Whatsapp Desktop")
                engine.runAndWait()
                continue
            except subprocess.CalledProcessError as e:
                print(f"Error launching WhatsApp Desktop: {e}")
                return False
            continue
        
        # Email - Gmail
        elif "open mail" in query.lower():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            engine.say("Opening Gmail")
            engine.runAndWait()
        
        # WhatsApp messaging
        elif "mssg" in query.lower():
            query = query.replace("mssg", "").strip()
            # Send WhatsApp message (replace with actual phone number)
            kit.sendwhatmsg("+910000000000", "Hello i am friday", 15, 3)
            time.sleep(10)
            engine.say(f"Message sent to {query}")
            engine.runAndWait()
        
        # Calculator functionality
        elif "calculate" in query.lower():
            query = query.replace("calculate", "").strip()
            result = eval(query)
            print(result)
            engine.say(f"The result of {query} is {result}")
            engine.runAndWait()
        
        # Web search
        elif "search" in query.lower():
            query = query.replace("search", "").strip()
            kit.search(query)
            engine.say(f"Searching for {query}")
            engine.runAndWait()
        
        # Thank you response
        elif "thank you" in query.lower():
            engine.say("You are welcome")
            engine.say("I am always here to help you")
            engine.runAndWait()
        
        # Exit commands
        elif "exit" in query.lower() or "bye" in query.lower():
            engine.say("Goodbye")
            engine.runAndWait()
            os.system("taskkill /f /im Code.exe")
            break
            
        # Default response for unrecognized commands
        else:
            engine.say("I am sorry, I did not understand")
            engine.runAndWait()
            continue

# Main execution
if __name__ == "__main__":
    start()
