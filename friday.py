# Import required libraries
import speech_recognition as sr  # For voice recognition
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
import requests              # For HTTP requests
import json                  # For JSON operations

# API keys for AI services (replace with your actual keys)
OPENAI_API_KEY = "your-openai-api-key"
DEEPSEEK_API_KEY = "your-deepseek-api-key"

def check_pyaudio():
    try:
        import pyaudio
        return True
    except ImportError:
        print("PyAudio is not installed. Installing PyAudio...")
        try:
            subprocess.check_call(['pip', 'install', 'pyaudio'])
            return True
        except subprocess.CalledProcessError:
            print("Error installing PyAudio. Please install it manually:")
            print("1. Open command prompt as administrator")
            print("2. Run: pip install pyaudio")
            if os.name == 'nt':  # Windows
                print("If above fails, download and install from:")
                print("https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio")
            return False

def get_chatgpt_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

def get_deepseek_response(prompt):
    url = "https://api.deepseek.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['text']

def listen():
    if not check_pyaudio():
        return ""
        
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # Reduced for better responsiveness
        r.energy_threshold = 400  # Adjusted for better voice detection
        r.dynamic_energy_threshold = True  # Adapts to ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection")
        return ""

def speak(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()

def process_command(query, is_voice=True):
    # Check for stop command before anything else
    if query == "stop":
        speak("Stopping assistant. Goodbye!") if is_voice else print("Stopping assistant. Goodbye!")
        return "stop"
        
    if is_voice and not query.startswith("hi friday"):
        return "continue"
        
    if is_voice:
        query = query.replace("hi friday", "").strip()
    
    if not query:
        speak("Hello, I am Friday your personal assistant. How can I help you?") if is_voice else print("Hello, I am Friday your personal assistant. How can I help you?")
        return "continue"
    
    # Process commands
    if "joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke) if is_voice else None
    
    elif "date" in query:
        today = datetime.date.today()
        date_string = today.strftime("%B %d, %Y")
        print(date_string)
        speak(f"The date is {date_string}") if is_voice else None
    
    # ... [Rest of the command processing remains the same, just add the conditional speak based on is_voice]
    # For brevity, keeping same command structure but adding the voice/text option
    
    else:
        msg = "I am sorry, I did not understand that command"
        speak(msg) if is_voice else print(msg)
    
    return "continue"

def start():
    engine = tts.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    greet = '''
                    ███████╗██████╗ ██╗██████╗  █████╗ ██╗   ██╗
                    ██╔════╝██╔══██╗██║██╔══██╗██╔══██╗╚██╗ ██╔╝
                    █████╗  ██████╔╝██║██║  ██║███████║ ╚████╔╝ 
                    ██╔══╝  ██╔══██╗██║██║  ██║██╔══██║  ╚██╔╝  
                    ██║     ██║  ██║██║██████╔╝██║  ██║   ██║   
                    ╚═╝     ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝
            '''
    print(greet)
    print("\nChoose your input method:")
    print("1. Voice Commands (Say 'Hi Friday' to activate)")
    print("2. Keyboard Input")
    
    while True:
        choice = input("Enter 1 or 2: ")
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 for voice commands or 2 for keyboard input.")
    
    if choice == "1":
        speak("Hi, I am Friday, your personal assistant. Say 'Hi Friday' to activate voice commands.")
        while True:
            query = listen()
            result = process_command(query, is_voice=True)
            if result == "stop":
                break
    else:
        print("Hi, I am Friday, your personal assistant. Type your commands (type 'stop' to exit).")
        while True:
            query = input("Enter command: ").lower()
            result = process_command(query, is_voice=False)
            if result == "stop":
                break

# Main execution
if __name__ == "__main__":
    start()
