from datasets import load_dataset
import json

# Load the dataset
dataset = load_dataset("Amod/mental_health_counseling_conversations")

# Extract the first 50 rows
sample_dataset = dataset['train']

# Save the dataset in JSONL format
with open("mental_health_dataset_sample.jsonl", "w") as f:
    for row in sample_dataset:
        json_line = json.dumps({"prompt": row["Context"], "completion": row["Response"]})
        f.write(json_line + "\n")
