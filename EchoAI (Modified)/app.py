import json

formatted_data = []

with open('training_data.jsonl', 'r') as file:
    for line in file:
        # Parse each line as a JSON object
        json_data = json.loads(line)
        # Create a new dictionary with the "messages" key
        formatted_line = {"messages": json_data["messages"]}
        # Append the formatted line to the list
        formatted_data.append(formatted_line)

# Now, 'formatted_data' holds a list of dictionaries in the desired format
