from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Choose role
role  = input("Choose role (aws, doctor, teacher, interviewer): ")
if role == "aws":
    instructions = """
        You are an AWS architect.
        Explain things simply with short sentences.
    """

elif role == "doctor":
    instructions = """
        You are a medical educator.
        Explain things simply with short sentences.
    """

elif role == "teacher":
    instructions = """
        You are a teacher.
        Explain things simply with short sentences.
    """
else:
    instructions = """
        You are a senior software engineering interviewer.
        Ask one question at a time.
        Wait for my answer.
        Provide feedback.
    """

# Chat loop
while True:
    # Get user input
    question = input("You: ")

    # Exit condition
    if question.lower() == 'exit':
        break

    # Empty question condition
    if question.lower().strip() == "":
        print("Please ask a question.")
        continue

    # Generate response
    response = client.responses.create(
        model="gpt-5",
        instructions=instructions,
        input=question
    )
    # Print usage
    print(response.usage)
    # Print response
    print("\nAI: ", response.output_text)
    print()
    