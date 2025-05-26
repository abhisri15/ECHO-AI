import json
from config import apiKey
formatted_data = []
import openai

with open('training_data.jsonl', 'r') as file:
    for line in file:
        # Parse each line as a JSON object
        json_data = json.loads(line)
        # Extract the prompt and completion
        prompt = json_data["prompt"]
        completion = json_data["completion"]
        # Create a list of dictionaries representing messages
        messages = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": completion}
        ]
        # Create a new dictionary with the "messages" key
        formatted_line = {"messages": messages}
        # Append the formatted line to the list
        formatted_data.append(formatted_line)

client=apiKey
# Initialize the OpenAI API client with your API key
openai.api_key = client

# Write the formatted data to a JSON file
with open('formatted_data.json', 'w') as outfile:
    json.dump(formatted_data, outfile)

# Use the OpenAI API to upload the data
response = openai.File.create(file=json_data, purpose='fine-tune')

print(response)