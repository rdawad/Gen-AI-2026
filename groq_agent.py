import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ.get("groq_api_key")
import os
from groq import Groq


client = Groq(
    api_key=os.environ.get(apikey),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a heplful assistant",
        },
        {
            "role": "user",
            "content": "what is Agentic Generative AI? explain as if a primary school student can understant",
        }
    ],
    model="llama-3.1-8b-instant",
    max_completion_tokens=1024,
    temperature=1,
)

print(chat_completion.choices[0].message.content)