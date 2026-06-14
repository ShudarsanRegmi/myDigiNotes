## LLMs and Agents Exploration 


<img width="997" height="290" alt="image" src="https://github.com/user-attachments/assets/904fe2f3-bfa3-475a-b52a-44cec03718db" />
<img width="682" height="490" alt="image" src="https://github.com/user-attachments/assets/3a9c2bb8-26d1-46f5-a95e-33cee8cd774e" />

- I thought, the security mechanism for not generating harmful content are external layers. But it seems, some guardrails are provided from training data itself.

## Three ways to Provide System Prompt to a model

**Using Ollama API**
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4",
  "messages": [
    {
      "role": "system",
      "content": "You are a cybersecurity tutor. Always explain concepts deeply."
    },
    {
      "role": "user",
      "content": "What is a buffer overflow?"
    }
  ]
}'
```

**Open WebUI**

In Open WebUI:

New Chat
Click the model settings / controls
Add a system prompt

Example:

You are a Linux mentor.
Provide examples for every concept.

Open WebUI will prepend that to every message sent to the model.


**Creating a Custom Ollama Model**

Step 1: Create a working directory
mkdir ollama-lab
cd ollama-lab
Step 2: Create a Modelfile
nano Modelfile

Paste:

FROM gemma4

SYSTEM """
You are a Linux mentor.

Rules:
- Explain step-by-step.
- Give terminal examples.
- Assume the user is curious and technical.
- Be concise but thorough.
"""

Save and exit.

Step 3: Build a new model
ollama create linux-gemma -f Modelfile

Expected output:

transferring model data
creating system layer
writing manifest
success
Step 4: Verify it exists
ollama list

You should see:

NAME
linux-gemma
gemma4
Step 5: Run it
ollama run linux-gemma

Ask:

What is a process?

You should notice the answer follows your Linux mentor persona.

<img width="578" height="344" alt="image" src="https://github.com/user-attachments/assets/2cda71de-5efd-4b7d-9c80-cfc28c6bce50" />

<img width="694" height="560" alt="image" src="https://github.com/user-attachments/assets/3b0bd434-b880-4baf-bb84-fcb12b6a83a2" />

<img width="972" height="382" alt="image" src="https://github.com/user-attachments/assets/2fcfe952-511e-48f4-aa3a-529ff49d6832" />

<img width="668" height="410" alt="image" src="https://github.com/user-attachments/assets/49adadc7-58d3-41da-b4b0-7da68da5dcfd" />


---

**Custom Model Creation in Openweb ui**
<img width="1108" height="720" alt="image" src="https://github.com/user-attachments/assets/7dd9db64-95cd-4898-9865-f3e0c7de601d" />



**Other Screenshots**
<img width="465" height="514" alt="image" src="https://github.com/user-attachments/assets/be2c2ba3-1d36-4742-875b-e761b6d4b00d" />

<img width="945" height="403" alt="image" src="https://github.com/user-attachments/assets/ad75fa79-805e-4e8a-a298-d4a96f3d2f59" />

<img width="1002" height="692" alt="image" src="https://github.com/user-attachments/assets/4e2aab82-13a0-432c-a09e-54ae936837a2" />

<img width="937" height="285" alt="image" src="https://github.com/user-attachments/assets/37ee460a-6d58-4627-b994-e2794f5f99bc" />

<img width="883" height="662" alt="image" src="https://github.com/user-attachments/assets/ab47ae27-1336-4ef1-8af1-874be23d75e1" />

<img width="1032" height="659" alt="image" src="https://github.com/user-attachments/assets/b26034a8-0b57-4c30-87ae-5b5a0e67912d" />


<img width="1009" height="466" alt="image" src="https://github.com/user-attachments/assets/bf22bcd7-20a2-4699-b634-fa118268c1e1" />


  

**Todo**

<img width="708" height="480" alt="image" src="https://github.com/user-attachments/assets/59188b28-aa43-435e-b3d7-e1056485399b" />

<img width="659" height="250" alt="image" src="https://github.com/user-attachments/assets/d0d5962c-f146-4889-b7d5-6ce728cadb38" />










