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

# Set your OpenAI API key
openai.api_key = "your_api_key"

# Function to fine-tune the model
def fine_tune_model(training_file):
    # Upload the training file
    response = openai.File.create(file=open(training_file, "rb"), purpose='fine-tune')
    training_file_id = response['id']

    print(f"Uploaded file with ID: {training_file_id}")

    # Create a fine-tuning job
    response = openai.FineTune.create(training_file=training_file_id, model="gpt-3.5-turbo-0613")
    fine_tune_job_id = response['id']

    print(f"Fine-tuning job created with ID: {fine_tune_job_id}")
    return fine_tune_job_id

# Fine-tune the model with the provided training data file
job_id = fine_tune_model("training_data.jsonl")
