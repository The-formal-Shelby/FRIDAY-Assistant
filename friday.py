# this us a comment 
import os
import requests
import speech_recognition as sr
import pyttsx3 as tts
from datetime import datetime, timedelta
import json
from typing import Optional, Dict, List
import encryption_lib
import wolframalpha
from dotenv import load_dotenv

load_dotenv()

class FridayAI:
    def __init__(self):
        # Initialize components
        self.engine = tts.init()
        self.recognizer = sr.Recognizer()
        self.voice_mode = True
        self.patient_data = {}
        self.medication_db = self._load_medication_db()
        self.symptom_checker = self._load_symptom_db()
        
        # Voice setup
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 180)
        
        # Medical APIs
        self.med_api = wolframalpha.Client(os.getenv('WOLFRAM_MED_KEY'))
        
        self.select_input_mode()

    def _load_medication_db(self) -> Dict:
        """Load medication database"""
        return {
            "paracetamol": {"uses": ["fever", "pain"], "dosage": "500mg every 4-6 hours"},
            "ibuprofen": {"uses": ["pain", "inflammation"], "dosage": "200-400mg every 4-6 hours"},
            "loratadine": {"uses": ["allergies"], "dosage": "10mg once daily"}
        }

    def _load_symptom_db(self) -> Dict:
        """Load symptom database"""
        return {
            "headache": {
                "common_causes": ["tension", "migraine", "dehydration"],
                "advice": "Rest in quiet room, drink water, consider pain relief"
            },
            "fever": {
                "common_causes": ["infection", "flu", "cold"],
                "advice": "Rest, hydrate, monitor temperature"
            }
        }

    def speak(self, text: str):
        """Enhanced TTS with emotional tone"""
        print(f"FRIDAY: {text}")
        # Adjust tone based on content
        if any(word in text.lower() for word in ["emergency", "alert", "warning"]):
            self.engine.setProperty('rate', 210)
            self.engine.setProperty('volume', 1.0)
        else:
            self.engine.setProperty('rate', 180)
            self.engine.setProperty('volume', 0.8)
            
        self.engine.say(text)
        self.engine.runAndWait()

    def medical_triage(self):
        """Interactive symptom checker"""
        self.speak("Let me help assess your symptoms. What are you experiencing?")
        
        symptoms = []
        while True:
            symptom = self.get_input("Describe one symptom at a time (or say 'done'): ")
            if symptom.lower() == 'done':
                break
            symptoms.append(symptom.lower())
            
            # Get immediate advice for each symptom
            if symptom in self.symptom_checker:
                advice = self.symptom_checker[symptom]["advice"]
                self.speak(f"For {symptom}: {advice}")
            else:
                self.speak(f"I'm noting {symptom}. Please continue or say 'done'")
        
        if symptoms:
            self.analyze_symptoms(symptoms)
        else:
            self.speak("No symptoms recorded")

    def analyze_symptoms(self, symptoms: List[str]):
        """Analyze collected symptoms"""
        self.speak(f"Analyzing your {len(symptoms)} symptoms...")
        
        # Check for medication matches
        suggested_meds = []
        for med, data in self.medication_db.items():
            if any(symptom in data["uses"] for symptom in symptoms):
                suggested_meds.append(med)
        
        # Generate report
        if suggested_meds:
            self.speak(f"Based on your symptoms, these may help: {', '.join(suggested_meds)}")
            for med in suggested_meds:
                self.speak(f"{med} dosage: {self.medication_db[med]['dosage']}")
        else:
            self.speak("I don't have specific medication suggestions")
        
        # Check for emergencies
        if any(s in ["chest pain", "difficulty breathing"] for s in symptoms):
            self.speak("EMERGENCY ALERT! These symptoms may be serious. Seek immediate medical help!")
        
        # Offer to save symptoms
        self.ask_followup()

    def ask_followup(self):
        """Follow-up questions"""
        response = self.get_input("Would you like me to save these symptoms for your doctor? (yes/no): ")
        if "yes" in response.lower():
            self.patient_data["symptoms"] = symptoms
            self.speak("Symptoms saved. Would you like to set a reminder to check on these?")
            
            reminder_resp = self.get_input("Set reminder? (yes/no): ")
            if "yes" in reminder_resp.lower():
                hours = self.get_input("In how many hours? (1-24): ")
                try:
                    reminder_time = datetime.now() + timedelta(hours=int(hours))
                    self.set_reminder(reminder_time, "Check your symptoms")
                except:
                    self.speak("Invalid time entered")

    def set_reminder(self, time: datetime, message: str):
        """Set a medication/symptom reminder"""
        # Implementation would use your preferred reminder system
        self.speak(f"Reminder set for {time.strftime('%I:%M %p')}: {message}")

    def process_command(self, command: str):
        """Enhanced command processor"""
        clean_cmd = command.replace("friday", "").strip().lower()
        
        if not clean_cmd:
            return
            
        # Medical commands
        if any(word in clean_cmd for word in ["symptom", "not feeling", "pain"]):
            self.medical_triage()
        elif "medicine" in clean_cmd or "medication" in clean_cmd:
            self.handle_medication_query(clean_cmd)
        elif "emergency" in clean_cmd:
            self.handle_emergency()
        # ... (keep other commands)
        
    def handle_medication_query(self, query: str):
        """Process medication-related queries"""
        if "side effects" in query:
            med = query.split("side effects")[0].strip()
            self.speak(f"Checking side effects for {med}...")
            # Would integrate with WolframAlpha API
        elif "dosage" in query:
            med = query.split("dosage")[0].strip()
            if med in self.medication_db:
                self.speak(f"{med} dosage: {self.medication_db[med]['dosage']}")
        else:
            self.speak("Please specify if you want dosage or side effects information")

    def handle_emergency(self):
        """Emergency protocol"""
        self.speak("EMERGENCY PROTOCOL ACTIVATED")
        # Would integrate with hospital systems
        self.speak("Alerting medical staff. Please stay calm.")

    # ... (keep existing input mode selection and other methods)

if __name__ == "__main__":
    assistant = FridayAI()
    assistant.speak("Medical Friday Assistant initialized")
    assistant.run()