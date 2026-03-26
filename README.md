# Groq-SDK-Chatbot

>While the Anthropic SDK was my initial choice, it does not offer a free tier. As a result, I opted for Groq as a cost-effective alternative.

A simple Python chatbot that uses the Groq API with the Llama 3.3 70B model to generate responses to user queries.

## Overview

This project demonstrates how to create a basic chatbot using the Groq API. The chatbot is powered by the Llama 3.3 70B model, which is available in the free tier.

## Features

- Simple command-line interface
- Uses Groq API with Llama 3.3 70B model
- Environment variable configuration for API key
- Easy to extend and customize

## Prerequisites

- Python 3.7 or higher
- Groq API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/anthropic-sdk-chatbot.git
   cd anthropic-sdk-chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install groq python-dotenv
   ```

3. Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot:
```bash
python Agent.py
```

The script will make a request to the Groq API with a sample question ("how to be confident?") and print the response.

## Customization

To change the question or add more functionality:

1. Modify the `messages` parameter in the `client.chat.completions.create()` call in `Agent.py`
2. You can add more messages to create a conversation history
3. Experiment with different models available in the Groq API

## Example

```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "The capital of France is Paris."},
        {"role": "user", "content": "What is the population of Paris?"}
    ]
)
```
