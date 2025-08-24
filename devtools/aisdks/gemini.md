
- Rate Limit Info - https://ai.google.dev/gemini-api/docs/rate-limits

<img width="747" height="429" alt="image" src="https://github.com/user-attachments/assets/169085de-768d-4135-a581-d1595a3073bb" />
<img width="757" height="283" alt="image" src="https://github.com/user-attachments/assets/7d71ee51-1324-4797-8b7c-3743c3582f9d" />


**Gemini Docs**
- https://ai.google.dev/gemini-api/docs


**Usage Dashboard**
- https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/metrics?project=pariapp-9bb3f



**API QuickStart**

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: GEMINI_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```
