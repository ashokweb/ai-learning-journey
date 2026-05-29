# Day 1 - OpenAI Chatbot

## Goal

Build my first AI application using the OpenAI API.

## What I Learned

### 1. OpenAI API Basics

* Created an OpenAI API account
* Generated an API key
* Learned how API requests work
* Sent prompts to GPT-5 and received responses

### 2. Environment Variables

* Learned why secrets should not be stored in source code
* Created a `.env` file
* Used `python-dotenv`
* Used `os.getenv()` to securely load API keys

### 3. Python Concepts

* Imports
* While loops
* If/Else conditions
* User input handling
* String operations

### 4. Prompt Engineering

* Used OpenAI `instructions`
* Created different AI personas:

  * AWS Architect
  * Medical Educator
  * Teacher
  * Software Engineering Interviewer
* Observed how AI responses change based on instructions

### 5. Token Usage

* Printed `response.usage`
* Learned that OpenAI billing is based on tokens
* Observed input, output, and total token counts

## Project Features

### AI Roles

Users can choose:

* AWS Architect
* Medical Educator
* Teacher
* Software Engineering Interviewer

### Chat Features

* Interactive chat loop
* Exit command
* Empty input validation
* Role-based responses
* Token usage display

## Example Architecture

User Input
↓
Python Application
↓
OpenAI SDK
↓
GPT-5 Model
↓
AI Response
↓
Display Response + Usage

## Key Concepts Learned

* API Keys
* Environment Variables
* Prompt Engineering
* AI Instructions
* Token Usage
* OpenAI SDK
* Basic AI Application Architecture

## Setup

```bash
cd day-01-openai-chatbot
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

Create a `.env` file in this folder:

```
OPENAI_API_KEY=your_api_key_here
```

## Run

```bash
python app.py
```

## Project Structure

```
day-01-openai-chatbot/
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## Status

✅ OpenAI API Connected

✅ Chatbot Working

✅ Multiple AI Roles Implemented

✅ Token Usage Tracking

🚀 Ready for Conversation Memory
