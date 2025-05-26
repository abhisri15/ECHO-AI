# Import necessary libraries
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from config import apiKey
import datetime
import sys
import random
import wikipedia

# Initialize global variables
chatStr = ""

# Set your OpenAI API key
openai.api_key = apiKey

# Fine-tuned model ID (replace with your actual fine-tuned model ID)
fine_tuned_model_id = "YOUR_FINE_TUNED_MODEL_ID"

# Define the chat function using the fine-tuned model
def chat(query):
    global chatStr
    chatStr += f"User: {query}\n EchoAI: "
    response = openai.ChatCompletion.create(
        model=fine_tuned_model_id,
        messages=[
            {"role": "system", "content": "You are EchoAI, a helpful assistant."},
            {"role": "user", "content": chatStr}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        reply = response['choices'][0]['message']['content']
        say(reply)
        chatStr += f"{reply}\n"
        return reply
    except Exception as e:
        print("Error:", e)

# Function to handle OpenAI prompts directly
def ai(prompt):
    response = openai.ChatCompletion.create(
        model=fine_tuned_model_id,
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        reply = response['choices'][0]['message']['content']
        print(reply)
        with open(f"OpenAI/prompt-{random.randint(1,999999999)}.txt", "w") as f:
            f.write(reply)
    except Exception as e:
        print("Error:", e)

# Function for text-to-speech
def say(text, speed=1.0, voice=None):
    engine = pyttsx3.init()
    if voice is not None:
        voices = engine.getProperty('voices')
        for v in voices:
            if v.name == voice:
                engine.setProperty('voice', v.id)
                break
    engine.setProperty('rate', speed * 125)
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Some Error Occurred:", e)
            return "Some Error Occurred."

# Main function
if __name__ == '__main__':
    print("Starting EchoAI...")
    say("Hello, I am Echo AI, how may I help you?", speed=1.7, voice='Microsoft Zira Desktop - English (United States)')
    while True:
        print("Listening...")
        query = takeVoiceCommand()
        sites = [["youtube", "https://youtube.com"], ["email", "https://gmail.com"], ["wikipedia", "https://wikipedia.com"],
                 ["open AI", "https://openai.com"], ["google", "https://google.com"]]

        # To open websites
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        # To play music
        if "play music" in query.lower():
            musicPath = "path_to_your_music_file.mp3"
            os.startfile(musicPath)

        # To check the time
        elif "time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            say(f"The time is {hour} hours, {min} minutes, and {sec} seconds")

        # Using OpenAI
        elif "artificial intelligence" in query.lower():
            ai(prompt=query)

        # To exit
        elif "exit" in query.lower() or "bye" in query.lower():
            say("Thank you for trying Echo AI, shutting down!")
            sys.exit()

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        # TODO: Add additional functionalities like opening apps, weather API, news API, etc.
