## AWS S3 Upload/Download Project

> This document shows how to make simple file upload and view/download system using aws s3 bucket as object storage. 

## Screenshots
<img width="373" height="329" alt="image" src="https://github.com/user-attachments/assets/4238ad71-b410-438e-b079-02a203447074" />

<img width="802" height="383" alt="image" src="https://github.com/user-attachments/assets/0b171d35-54b3-4f8c-a8e5-87e576cd863a" />

### Project Structure
```bash
├── app.js
├── models
│   └── File.js
├── package.json
├── package-lock.json
└── public
    └── index.html
```


---
**app.js**
```js
import express from "express";
import dotenv from "dotenv";
import mongoose from "mongoose";
import cors from "cors";
import { S3Client, PutObjectCommand, GetObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import File from "./models/File.js";

dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static("public"));

// --- MongoDB ---
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => console.log("✅ MongoDB Connected"))
  .catch((err) => console.error("MongoDB Error:", err));

// --- AWS S3 ---
const s3 = new S3Client({
  region: process.env.AWS_REGION,
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  },
});

// --- Generate presigned upload URL ---
app.post("/api/generate-upload-url", async (req, res) => {
  try {
    const { fileName, fileType } = req.body;
    if (!fileName || !fileType) throw new Error("fileName or fileType missing");

    const key = `uploads/${Date.now()}_${fileName}`;

    const command = new PutObjectCommand({
      Bucket: process.env.S3_BUCKET,
      Key: key,
      ContentType: fileType,
    });

    const uploadUrl = await getSignedUrl(s3, command, { expiresIn: 3600 }); // 1 hr
    res.json({ uploadUrl, fileKey: key });
  } catch (err) {
    console.error("Upload URL error:", err);
    res.status(500).json({ message: err.message });
  }
});

// --- Save file metadata after upload ---
app.post("/api/save-file", async (req, res) => {
  try {
    const newFile = new File(req.body);
    const saved = await newFile.save();
    res.json(saved);
  } catch (err) {
    console.error("Save metadata error:", err);
    res.status(500).json({ message: err.message });
  }
});

// --- Generate presigned download URL ---
app.get("/api/file/:id", async (req, res) => {
  try {
    const file = await File.findById(req.params.id);
    if (!file) return res.status(404).json({ message: "File not found" });

    const command = new GetObjectCommand({
      Bucket: process.env.S3_BUCKET,
      Key: file.fileKey,
    });

    const downloadUrl = await getSignedUrl(s3, command, { expiresIn: 600 }); // 10 min
    res.json({ downloadUrl });
  } catch (err) {
    console.error("Download URL error:", err);
    res.status(500).json({ message: err.message });
  }
});

// --- List all files ---
app.get("/api/files", async (req, res) => {
  try {
    const files = await File.find().sort({ uploadedAt: -1 });
    res.json(files);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// --- Start server ---
app.listen(process.env.PORT, () => console.log(`🚀 Server running at http://localhost:${process.env.PORT}`));


```

**models/File.js**
```js
import mongoose from "mongoose";

const fileSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: String,
  uploadedBy: String,
  courseId: String,
  semesterId: String,
  classId: String,
  fileKey: { type: String, required: true }, // S3 object key
  fileType: String,
  tags: [String],
  likes: [String],
  isVerified: { type: Boolean, default: false },
  sharedBy: String,
  uploadedAt: { type: Date, default: Date.now },
});

export default mongoose.model("File", fileSchema);


```

**public/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AWS S3 Upload Demo</title>
</head>
<body>
<h2>Upload File</h2>
<form id="uploadForm">
  <input type="text" id="title" placeholder="Title" required /><br />
  <textarea id="desc" placeholder="Description"></textarea><br />
  <input type="file" id="fileInput" required /><br />
  <button type="submit">Upload</button>
</form>

<h3>Files</h3>
<div id="fileList"></div>

<script>
const apiBase = "http://localhost:5001/api";

async function loadFiles() {
  const res = await fetch(`${apiBase}/files`);
  const files = await res.json();
  const list = document.getElementById("fileList");
  list.innerHTML = files.map(f => `
    <div>
      <b>${f.title}</b> - ${f.fileType} <br>
      <button onclick="getDownloadUrl('${f._id}')">View / Download</button>
    </div><hr>
  `).join("");
}

async function getDownloadUrl(fileId) {
  const res = await fetch(`${apiBase}/file/${fileId}`);
  const data = await res.json();
  if (data.downloadUrl) window.open(data.downloadUrl, "_blank");
  else alert("Unable to get download URL");
}

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = document.getElementById("fileInput").files[0];
  const title = document.getElementById("title").value;
  const description = document.getElementById("desc").value;

  // 1️⃣ Get presigned upload URL
  const res = await fetch(`${apiBase}/generate-upload-url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ fileName: file.name, fileType: file.type })
  });
  const { uploadUrl, fileKey } = await res.json();

  // 2️⃣ Upload file directly to S3
  await fetch(uploadUrl, {
    method: "PUT",
    headers: { "Content-Type": file.type },
    body: file
  });

  // 3️⃣ Save metadata in MongoDB
  await fetch(`${apiBase}/save-file`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title, description, fileKey, fileType: file.type, uploadedBy: "user123"
    })
  });

  alert("File uploaded successfully!");
  document.getElementById("fileInput").value = "";
  loadFiles();
});

loadFiles();
</script>
</body>
</html>

```
**.env**
```bash
AWS_ACCESS_KEY_ID=AKIxxxxxxxxxxxxxNXM2
AWS_SECRET_ACCESS_KEY=Niwsh5xxxxxx8hot/tfpSxxxxxxxxhUinP
AWS_REGION=us-east-1
S3_BUCKET=shud-s31
MONGO_URI=mongodb://localhost:27017/awsupload
PORT=5001
```
---

### Following S3 Configurations needs to be done

Here’s a **concise summary** of all the **S3-side configurations** we did to make your classroom management system’s file upload feature work securely and smoothly:

---

### **Created an S3 Bucket**

* Example: `shud-s31`
* Region: `us-east-1`
* Used as **object storage** for all user-uploaded files (notes, images, assignments, etc.)
* Default public access was **blocked** to keep data private.

---

### **Configured AWS IAM Credentials**

* Created an **IAM User** (e.g., `s3-upload-user`) with **programmatic access**.
* Attached the following **IAM policy** to allow secure read/write operations:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::shud-s31/uploads/*"
    }
  ]
}
```

* From this user, generated **Access Key ID** and **Secret Access Key**, used by your backend SDK.

#### **Access Control & Security**

* Bucket’s **public access blocked globally** — no file is public by default.

#### CORS Configuration
Enabled the frontend (React app on `http://localhost:5001`) to upload directly using **pre-signed URLs**:

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST"
        ],
        "AllowedOrigins": [
            "http://localhost:5001"
        ],
        "ExposeHeaders": [
            "ETag"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

### Explanation

## 🧩 1. AWS SDK v3 — Core Concepts

The **AWS SDK for JavaScript v3** is modular — meaning you only import what you use.

In v2:

```js
const AWS = require('aws-sdk');
const s3 = new AWS.S3();
```

In v3 (modular, ESM-friendly):

```js
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
```

This design is faster and more lightweight because it doesn’t load all AWS services.

---

### **🔧 S3Client Initialization**

This client is your authenticated gateway to AWS S3.

```js
const s3 = new S3Client({
  region: "us-east-1",
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  },
});
```

* `region` must match your S3 bucket’s region (otherwise → “PermanentRedirect” error).
* The credentials allow you to sign and authorize API requests to S3.

---

### **📤 Uploading Objects — `PutObjectCommand`**

```js
import { PutObjectCommand } from "@aws-sdk/client-s3";

const command = new PutObjectCommand({
  Bucket: "my-bucket",
  Key: "uploads/file.pdf",
  Body: fileBuffer,
  ContentType: "application/pdf",
});
await s3.send(command);
```

This **actually uploads** the file bytes to S3.
If you’re uploading directly from the backend, you’d use this command.

---

### **📥 Fetching Objects — `GetObjectCommand`**

```js
import { GetObjectCommand } from "@aws-sdk/client-s3";

const command = new GetObjectCommand({
  Bucket: "my-bucket",
  Key: "uploads/file.pdf",
});
const response = await s3.send(command);
```

This returns a stream of file data. You could pipe this to the browser, but it’s often better to generate a **temporary signed URL** instead.

---

### **🧾 Signed URLs — via `getSignedUrl`**

```js
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
const url = await getSignedUrl(s3, command, { expiresIn: 3600 });
```

This creates a **URL that contains a digital signature** (computed with your secret access key).
That URL is valid for a specific time (`expiresIn` seconds).
Once it expires — S3 rejects the request.

---

## ⚙️ 2. Separation of Object Storage and Metadata

Your current design smartly separates:

* **Binary files** → stored in S3
* **Metadata** → stored in MongoDB

For example:

| Layer        | Stored In | Example Data                                            |
| ------------ | --------- | ------------------------------------------------------- |
| File bytes   | S3        | `uploads/1761309757946_notes.pdf`                       |
| File details | MongoDB   | `{ title, description, fileKey, uploadedBy, fileType }` |

This approach:
✅ Keeps DB light (no file blobs)
✅ Allows fast file serving via CDN/S3
✅ Makes metadata searchable and filterable

---

## 🚀 3. How the Upload System Works (Architectural Flow)

Let’s visualize your final working flow:

### 🧭 **Step-by-Step Data Flow**

1. **Frontend** → asks backend for a signed upload URL
   `POST /api/generate-upload-url`

2. **Backend** → calls AWS SDK

   * Creates a `PutObjectCommand`
   * Uses `getSignedUrl()` to sign it using your AWS credentials
   * Returns a temporary URL to frontend

3. **Frontend** → uploads file **directly to S3** using that URL

   ```js
   await fetch(uploadUrl, { method: "PUT", body: file });
   ```

   ⚡ No file bytes touch your server — fast and scalable!

4. **Frontend** → then notifies backend to store metadata in MongoDB
   `POST /api/save-file`

5. **When viewing** → frontend calls
   `GET /api/file/:id`
   → backend fetches metadata
   → generates **signed GET URL** (temporary download link)

---

## 🔒 4. What Was the Initial Problem?

Initially, you had this setup:

```
Frontend  →  Backend  →  S3
```

You directly uploaded to S3 via backend, stored the *public URL* (like `https://bucket.s3.amazonaws.com/file.pdf`).

This failed because:

* Your S3 bucket was **private** by default (which is good).
* When users tried to access the URL → **AccessDenied** XML error.

---

### ❌ Options You Had:

| Option             | Description                             | Security            |
| ------------------ | --------------------------------------- | ------------------- |
| Make bucket public | Anyone on the internet can access files | ❌ Bad               |
| Use presigned URLs | Signed, time-limited access             | ✅ Secure & Scalable |

So, instead of exposing S3 publicly, we introduced **presigned URLs**:

* Time-bound
* User-specific
* Region-correct
* Automatically signed by AWS SDK

---

## 🔐 5. How Signing Works (Architectural Level)

Let’s unpack the magic under the hood.

### 🧠 **What is a "Signed URL"?**

A **presigned URL** includes:

* Object path (`Key`)
* AWS credentials (Access Key)
* Timestamp (`X-Amz-Date`)
* Expiry time (`X-Amz-Expires`)
* Digital signature (`X-Amz-Signature`)

Example:

```
https://my-bucket.s3.amazonaws.com/uploads/file.pdf?
X-Amz-Algorithm=AWS4-HMAC-SHA256&
X-Amz-Credential=AKIA.../20251024/us-east-1/s3/aws4_request&
X-Amz-Date=20251024T124237Z&
X-Amz-Expires=3600&
X-Amz-Signature=abcf923dbd...
```

---

### ⚙️ **How AWS Signs the URL**

1. The SDK takes your secret access key.
2. It creates a **hash** (HMAC-SHA256) of:

   ```
   [HTTP Verb] + [Canonical URI] + [Headers] + [Date] + [Credentials]
   ```
3. That hash is appended as `X-Amz-Signature`.

When S3 receives the request, it:

* Recomputes the hash using your AWS secret key on the server-side.
* Compares both signatures.
* Grants access if they match **and** not expired.

---

### ✅ Why It’s Secure

* Only your server (with AWS credentials) can generate valid signatures.
* URLs expire quickly, reducing exposure.
* No AWS keys are ever exposed in frontend code.
* You can scope access per object, per user, per time window.

---

## ⚡ 6. Why Frontend Direct Upload is Better

| Aspect      | Old Way (Server Upload)              | New Way (Presigned Upload)   |
| ----------- | ------------------------------------ | ---------------------------- |
| Server load | Heavy (file streamed through server) | Light (frontend → S3 direct) |
| Scalability | Poor                                 | Excellent                    |
| Latency     | High                                 | Low                          |
| Security    | Credentials risk if exposed          | Secure, short-lived URLs     |
| Cost        | Extra data transfer through EC2      | Direct S3 transfer (cheaper) |

---

## 🔄 7. Summary

| Concept                | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| **S3Client**           | Authenticated interface to AWS S3                      |
| **PutObjectCommand**   | Upload object (or generate presigned PUT URL)          |
| **GetObjectCommand**   | Download object (or generate presigned GET URL)        |
| **getSignedUrl()**     | Signs your S3 request with AWS credentials             |
| **Presigned URL**      | Temporary, signed access to an S3 object               |
| **AccessDenied issue** | Happens when trying to access private S3 URLs directly |
| **Solution**           | Use presigned URLs for secure, temporary access        |

---


