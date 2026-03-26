import os
from dotenv import load_dotenv
from groq import Groq

# Load your API key from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # free tier model
    messages=[
        {"role": "user", "content": "how to be confident?"}
    ]
)

print(response.choices[0].message.content)