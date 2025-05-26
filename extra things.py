##### Simple Base Code
'''
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__== '__main__':
    print("PyCharm")
    say("Hello I am Echo AI")
'''
#----------------------------------------------------------------

##### To check the list of voices available
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for v in voices:
    print(v.name)
'''
#----------------------------------------------------------------

##### You can make the computer Speak anything you type
'''
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the word you want computer to speak out: ")
    str = input()
    speaker.Speak(str)
'''
#----------------------------------------------------------------

import openai
import os
import json
from config import apiKey

openai.api_key = apiKey

# Upload the dataset
response = openai.File.create(
  file=open("mental_health_dataset_sample.jsonl"),
  purpose='fine-tune'
)

# Extract file ID
file_id = response['id']
print(f"Uploaded file with ID: {file_id}")

# Fine-tune the model
fine_tune_response = openai.FineTune.create(
  training_file=file_id,
  model="davinci-003",
  n_epochs=4
)

# Extract fine-tuned model ID
fine_tuned_model_id = fine_tune_response['fine_tuned_model']
print(f"Fine-tuned model ID: {fine_tuned_model_id}")

