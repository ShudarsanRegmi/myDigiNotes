# Google AI Studio

## Tooling

We've to define our funciton(tools) like this:

<img width="699" height="523" alt="image" src="https://github.com/user-attachments/assets/cf7ee3cc-9c72-4a83-bcb2-87069cf560b0" />


```json
[
  {
    "name": "getWeather",
    "description": "gets the weather for a requested city",
    "parameters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string"
        }
      },
      "propertyOrdering": [
        "city"
      ]
    }
  }
]

```

<img width="1271" height="678" alt="image" src="https://github.com/user-attachments/assets/49c4bd79-84ac-4f2b-bf2f-8444b4eb3ec9" />





