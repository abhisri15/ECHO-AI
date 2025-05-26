# pip install speechrecognition
# pip install wikipedia
# pip install openai

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

chatStr=""
def chat(query):
    global chatStr
    openai.api_key = apiKey
    chatStr += f"Abhi: {query}\n EchoAI: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]

        # with open(f"OpenAI/prompt- {random.randint(1,999999999)}", "w") as f:
        with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)

    except Exception as e:
        print("Error")


def ai(prompt):
    openai.api_key = apiKey
    text = f"OpenAI response for prompt:\n {prompt} \n ----------------------------\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0].text)
        text += response["choices"][0].text
        if not os.path.exists("OpenAI"):
            os.mkdir("OpenAI")

        # with open(f"OpenAI/prompt- {random.randint(1,999999999)}", "w") as f:
        with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)

    except Exception as e:
        print("Error")



def say(text, speed=1.0, voice=None):
    engine = pyttsx3.init()

    # Change the voice (if specified)
    if voice is not None:
        voices = engine.getProperty('voices')
        for v in voices:
            if v.name == voice:
                engine.setProperty('voice', v.id)
                break

    # Adjust the default rate of speech
    engine.setProperty('rate', speed * 125)  # Adjust the multiplier for desired speed

    engine.say(text)
    engine.runAndWait()

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
            return "Some Error Occurred."

if __name__ == '__main__':
    print("PyCharm")
    say("Hello, I am Echo AI, how may I help you?", speed=1.7, voice='Microsoft Zira Desktop - English (United States)')
    while True:
        print("Listening...")
        query = takeVoiceCommand()
        sites=[["youtube","https://youtube.com"],["email","https://gmail.com"],["wikipedia","https://wikipedia.com"]
        ,["open AI","https://openai.com"],["google","https://google.com"]]

        # TO OPEN WEBSITES
        # todo: ADD MORE WEBSITES
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        # TO PLAY MUSIC
        # todo: ADD MUSIC
        if "play music" in query.lower():
            musicPath="F:\IIIT Bhubaneswar\ML\EchoAI\downfall-21371.mp3"
            os.startfile(musicPath)
            # or use os.system(f"open{musicPath}")

        # TO CHECK TIME
        elif "time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            say(f"The time is {hour}Hours, {min}minutes, {sec}seconds")

        # USING OPENAI
        elif "artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        # TO EXIT
        elif "exit" or "bye" in query.lower():
            say("Thank you for trying ECHO AI, shutting down!")
            sys.exit()

        elif "reset chat".lower() in query.lower():
            chatStr=""

        else:
            print("Chatting...")
            chat(query, chatStr)

        # todo: CREATE LOOP, TO OPEN APPS
        # todo: USE WEATHER API - "weatherapi.com" - integrate this
        # todo: USE NEWS API - "newsapi.com" - integrate this
        # todo: try new stuffs