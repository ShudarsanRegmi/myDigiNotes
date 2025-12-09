# Documents some important things to know about gemini apis/sdks

<img width="776" height="442" alt="image" src="https://github.com/user-attachments/assets/a33803b2-feaa-488d-afee-fb93c8dcd61e" />

- Gemini supports openai library

```python
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)

```



