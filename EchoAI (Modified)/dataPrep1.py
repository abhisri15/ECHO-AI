import openai
import json
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Amod/mental_health_counseling_conversations")

# Prepare the dataset in the required format
def prepare_data(dataset):
    formatted_data = []
    for example in dataset['train']:
        prompt = example['Context']  # Adjust according to actual dataset structure
        completion = example['Response']  # Adjust according to actual dataset structure
        formatted_data.append({"prompt": prompt, "completion": completion})
    return formatted_data

# Save the prepared data to a JSONL file
prepared_data = prepare_data(dataset)
with open("training_data.jsonl", "w") as f:
    for item in prepared_data:
        f.write(json.dumps(item) + "\n")

print("Data preparation complete. The prepared data has been saved to training_data.jsonl.")
