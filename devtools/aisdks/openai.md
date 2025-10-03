## OpenAI SDK


```py
# simple_openai_example.py

from openai import OpenAI

# 🔑 Hardcode your API key here
OPENAI_API_KEY = "sk-proj-BdQexxxxxxxxxxxxxxxxxxxroNVeF34A"

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Send a simple chat request
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is heroku?"}
    ]
)

# Print the model's reply
print(response.choices[0].message.content)
```

<img width="1354" height="754" alt="image" src="https://github.com/user-attachments/assets/037178d9-e9f8-46f0-a259-e4ab43a35b0a" />
