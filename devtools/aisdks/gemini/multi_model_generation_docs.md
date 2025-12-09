# Multimodel Image generation

## Models that can be used for Image generation
- Gemini 2.5 Flash(aka Nano Banana)
- Gemini 3 Pro Preview (aka Nano Banana Pro)



> They can take multimodel input and generate image. Have iterative refinement capabilities. High fidelity rendering.

## Image Generation (text to image)

```python
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

## Image Editing

```python
prompt = (
    "Create a picture of my cat eating a nano-banana in a "
    "fancy restaurant under the Gemini constellation",
)

image = Image.open("/path/to/cat_image.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, image],
)
```

## Some Important Points:
- Supports Multi Turn Image Editing
- Upto 14 reference images can be supplied
- Image generation can be grounded wtih google search
- Docs has provided prompting guides as well as several other examples

# Image Understanding

>Gemini unlocks a wide range of image processing and computer vision tasks including but not limited to image captioning, classification, and visual question answering without having to train specialized ML models.

## Passing Images to API

There are two methods:
- Passing inline image data (supports upto 20MB)
- Uploading using file API(recommended for large file sizes)

  ```python
    from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
  )

  print(response.text)
  ```


## Uploading Using file API

```python
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "Caption this image."],
)

print(response.text)
```

## Important Points
- We can also prompt with multiple Inputs
- **Object Detection**: From Gemini 2.0 onwards, models are further trained to detect objects in an image and get their bounding box coordinates.
- **Segmentation**: Starting with Gemini 2.5, models not only detect items but also segment them and provide their contour masks.

 ![segmentation](https://github.com/user-attachments/assets/8f004d19-76cf-4a6d-8ca9-aafa6d44cc78)

- Gemini 2.0 models are further trained to support enhanced object detection.
- Gemini 2.5 models are further trained to support enhanced segmentation in addition to object detection.
- Gemini 2.5 Pro/Flash, 2.0 Flash, 1.5 Pro, and 1.5 Flash support a maximum of 3,600 image files per request.


## Image Token Calculation
- Gemini 1.5 Flash and Gemini 1.5 Pro: 258 tokens if both dimensions <= 384 pixels. Larger images are tiled (min tile 256px, max 768px, resized to 768x768), with each tile costing 258 tokens.
- Gemini 2.0 Flash and Gemini 2.5 Flash/Pro: 258 tokens if both dimensions <= 384 pixels. Larger images are tiled into 768x768 pixel tiles, each costing 258 tokens.


# Thinking

> The Gemini 3 and 2.5 series models use an internal "thinking process" that significantly improves their reasoning and multi-step planning abilities, making them highly effective for complex tasks such as coding, advanced mathematics, and data analysis.

## Important Points
- Thought summaries can be enabled in the api config (raw thoughts of model)
- Gemini3 has thinking levels `high` and `low` while other previous models has thinking budget parameter
- In order to enable maintaining thought context across multi-turn interactions, Gemini returns thought signatures, which are encrypted representations of the model's internal thought process.
- When thinking is turned on, response pricing is the sum of output tokens and thinking tokens. You can get the total number of generated thinking tokens from the thoughtsTokenCount field
