# Gemini Docs Walkthrough


## Initialization Script

```python
import { GoogleGenAI } from "@google/genai";
const ai = new GoogleGenAI({});
```

## Text generation

> The Gemini API can generate text output from various inputs, including text, images, video, and audio, leveraging Gemini models.

```python
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "How does AI work?",
  });
  console.log(response.text);
}

await main();

```
- `await ai.models.generateContent({params_json})`
- gemini-2.5-flash has thinking enabled by default, set config to give thinkingBudgest=0

## Provide System Instructions
- parameters like system instructions, temperature, etc. can be configured through config key
  
```python
const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Hello there",
    config: {
      systemInstruction: "You are a cat. Your name is Neko.",
    },
  });
```

Supports Multimodel Input

The Gemini API supports multimodal inputs, allowing you to combine text with media files. The following example demonstrates providing an image:

```python
async function main() {
  const image = await ai.files.upload({
    file: "/path/to/organ.png",
  });
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: [
      createUserContent([
        "Tell me about this instrument",
        createPartFromUri(image.uri, image.mimeType),
      ]),
    ],
  });
```

## Streaming the response

```python
const response = await ai.models.generateContentStream({
    model: "gemini-2.5-flash",
    contents: "Explain how AI works",
  });
```

Mutli turn Conversations

```python
async function main() {
  const chat = ai.chats.create({
    model: "gemini-2.5-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const response1 = await chat.sendMessage({
    message: "I have 2 dogs in my house.",
  });
  console.log("Chat response 1:", response1.text);

  const response2 = await chat.sendMessage({
    message: "How many paws are in my house?",
  });
  console.log("Chat response 2:", response2.text);
}

```

## Streaming in Multi Turn Conversations

```python
const stream1 = await chat.sendMessageStream({
    message: "I have 2 dogs in my house.",
  });
```

## Supporting Models
- All gemini models support text generation

## Best Practices
- for basic generation, use zero shot prompting
- For more tailored outputs use, system instructions, provide examples(few shots prompting)

## Structured Output
- Forcing the model to generate structure output
- You can configure Gemini models to generate responses that adhere to a provided JSON Schema. This capability guarantees predictable and parsable results, ensures format and type-safety, enables the programmatic detection of refusals, and simplifies prompting.
- Applications of structured output: data extraction, structured classification, agentic workflows
- Pydantic in python or ZodSchema in js can be used to define the format..

**JavaScript Zod Schema**

```js
const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

```

**Pydantic model**

```python
class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

```

## Refernces
- [Text Generation](https://ai.google.dev/gemini-api/docs/text-generation#javascript_4)
- [Structured Output](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe#python_2)








