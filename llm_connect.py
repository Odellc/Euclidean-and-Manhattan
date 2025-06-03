import openai
from dotenv import load_dotenv
import os


load_dotenv()

openai.api_key = os.getenv("API_KEY")

# client = OpenAI(api_key=os.getenv("API_KEY")) # Replace "YOUR_API_KEY" with your actual API key
# Your code that uses the client will now work

# Example: Chat completions API
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write a short poem about the moon."}
    ]
)

print(completion.choices[0].message.content)


