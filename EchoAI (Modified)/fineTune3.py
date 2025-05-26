import time
import openai

# Function to check the status of the fine-tuning job
def check_fine_tune_status(job_id):
    response = openai.FineTune.retrieve(id=job_id)
    status = response['status']
    print(f"Fine-tuning job status: {status}")
    return status

# Function to get the fine-tuned model ID
def get_fine_tuned_model_id(job_id):
    response = openai.FineTune.retrieve(id=job_id)
    model_id = response['fine_tuned_model']
    print(f"Fine-tuned model ID: {model_id}")
    return model_id

# Check the status of the fine-tuning job
while True:
    status = check_fine_tune_status(job_id)
    if status == 'succeeded':
        fine_tuned_model_id = get_fine_tuned_model_id(job_id)
        break
    elif status == 'failed':
        raise Exception("Fine-tuning job failed.")
    time.sleep(60)  # Wait for a minute before checking the status again
