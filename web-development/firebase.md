# Developing Auth System Using Firebase


## Firebase Platform
1. Create firebase project
2. Go to `Authentication` and select providers (eg. Google, facebook, email, github, etc.)

## Enabling Github SignIn


![image](https://github.com/user-attachments/assets/beb4fee1-a60d-4c10-ba6e-a7b58638e26a)

### Register new app(oauth) in github
![image](https://github.com/user-attachments/assets/d3c93402-7608-4060-a3a0-fe3ca67a35ec)

- `https://<app-id>.firebaseapp.com`
- copy authorization callback URL
- Register application
- Copy and client id and generate new secret
- Fill the client id and secret to create github signin for your firebase app

![image](https://github.com/user-attachments/assets/4c81fd3a-530c-4dd5-b4bf-20fd3999ed46)


## Workflow

![image](https://github.com/user-attachments/assets/5d99bed9-bc41-4611-8094-604e91f19327)


## Codes

### Front End

`firebase.js`
```js
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import {  GoogleAuthProvider } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDk0ZnuLNA-_PrafkEROE3-1XiD_-KhPj4",
  authDomain: "classmgmt-aa87d.firebaseapp.com",
  projectId: "classmgmt-aa87d",
  storageBucket: "classmgmt-aa87d.firebasestorage.app",
  messagingSenderId: "60650241423",
  appId: "1:60650241423:web:aca89a25df9e7d09291ffa"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export {auth};

```

`Register.jsx` - React Component

```js
import React, { useState } from "react";
import { auth } from "../firebase";
import { createUserWithEmailAndPassword, signInWithPopup, GoogleAuthProvider, GithubAuthProvider } from "firebase/auth";
import { useNavigate } from "react-router-dom";
import { FaGoogle, FaGithub, FaEnvelope, FaLock } from "react-icons/fa";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      console.log("User Registered:", userCredential.user);
      navigate("/");
    } catch (error) {
      console.error("Registration Error:", error.message);
      setError(error.message);
    }
  };

  const handleGoogleLogin = async () => {
    setError("");
    const provider = new GoogleAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      console.log("Google Login Success:", result.user);
      navigate("/");
    } catch (error) {
      console.error("Google Login Error:", error.message);
      setError(error.message);
    }
  };

  const handleGithubLogin = async () => {
    setError("");
    const provider = new GithubAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      console.log("GitHub Login Success:", result.user);
      navigate("/");
    } catch (error) {
      console.error("GitHub Login Error:", error.message);
      setError(error.message);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-8 bg-white shadow-md rounded-lg">
      <h2 className="text-2xl font-semibold text-center mb-6 text-gray-700">Register</h2>

      {error && (
        <div className="bg-red-100 text-red-700 p-3 mb-6 rounded-md text-sm">
          {error}
        </div>
      )}

      <form onSubmit={handleRegister} className="flex flex-col space-y-4">
        <div className="flex items-center border border-gray-300 rounded-md overflow-hidden">
          <div className="bg-gray-100 p-3">
            <FaEnvelope className="text-gray-500" />
          </div>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="flex-1 p-3 focus:outline-none"
          />
        </div>

        <div className="flex items-center border border-gray-300 rounded-md overflow-hidden">
          <div className="bg-gray-100 p-3">
            <FaLock className="text-gray-500" />
          </div>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="flex-1 p-3 focus:outline-none"
          />
        </div>

        <button type="submit" className="bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition">
          Register
        </button>
      </form>

      <div className="flex items-center my-6">
        <div className="flex-grow border-t border-gray-300"></div>
        <span className="mx-4 text-gray-500 text-sm">OR</span>
        <div className="flex-grow border-t border-gray-300"></div>
      </div>

      <div className="flex flex-col space-y-4">
        <button
          onClick={handleGoogleLogin}
          className="flex items-center justify-center bg-red-500 text-white py-2 rounded-md hover:bg-red-600 transition"
        >
          <FaGoogle className="mr-2" /> Continue with Google
        </button>

        <button
          onClick={handleGithubLogin}
          className="flex items-center justify-center bg-gray-800 text-white py-2 rounded-md hover:bg-gray-900 transition"
        >
          <FaGithub className="mr-2" /> Continue with GitHub
        </button>
      </div>
    </div>
  );
};

export default Register;

```

`Login.jsx` - React Component

```js
import React, { useState } from "react";
import { auth } from "../firebase";
import { signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider, GithubAuthProvider } from "firebase/auth";
import { useNavigate } from "react-router-dom";
import { FaGoogle, FaGithub, FaEnvelope, FaLock } from "react-icons/fa";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      console.log("User Logged In:", userCredential.user);
      navigate("/");
    } catch (error) {
      console.error("Login Error:", error.message);
      setError(error.message);
    }
  };

  const handleGoogleLogin = async () => {
    setError("");
    const provider = new GoogleAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      console.log("Google Login Success:", result.user);
      navigate("/");
    } catch (error) {
      console.error("Google Login Error:", error.message);
      setError(error.message);
    }
  };

  const handleGithubLogin = async () => {
    setError("");
    const provider = new GithubAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      console.log("GitHub Login Success:", result.user);
      navigate("/");
    } catch (error) {
      console.error("GitHub Login Error:", error.message);
      setError(error.message);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-8 bg-white shadow-md rounded-lg">
      <h2 className="text-2xl font-semibold text-center mb-6 text-gray-700">Login</h2>

      {error && (
        <div className="bg-red-100 text-red-700 p-3 mb-6 rounded-md text-sm">
          {error}
        </div>
      )}

      <form onSubmit={handleLogin} className="flex flex-col space-y-4">
        <div className="flex items-center border border-gray-300 rounded-md overflow-hidden">
          <div className="bg-gray-100 p-3">
            <FaEnvelope className="text-gray-500" />
          </div>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="flex-1 p-3 focus:outline-none"
          />
        </div>

        <div className="flex items-center border border-gray-300 rounded-md overflow-hidden">
          <div className="bg-gray-100 p-3">
            <FaLock className="text-gray-500" />
          </div>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="flex-1 p-3 focus:outline-none"
          />
        </div>

        <button type="submit" className="bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition">
          Login
        </button>
      </form>

      <div className="flex items-center my-6">
        <div className="flex-grow border-t border-gray-300"></div>
        <span className="mx-4 text-gray-500 text-sm">OR</span>
        <div className="flex-grow border-t border-gray-300"></div>
      </div>

      <div className="flex flex-col space-y-4">
        <button
          onClick={handleGoogleLogin}
          className="flex items-center justify-center bg-red-500 text-white py-2 rounded-md hover:bg-red-600 transition"
        >
          <FaGoogle className="mr-2" /> Continue with Google
        </button>

        <button
          onClick={handleGithubLogin}
          className="flex items-center justify-center bg-gray-800 text-white py-2 rounded-md hover:bg-gray-900 transition"
        >
          <FaGithub className="mr-2" /> Continue with GitHub
        </button>
      </div>
    </div>
  );
};

export default Login;

```

## Back End

`firebaseAdmin.js`
```js
var admin = require("firebase-admin");

var serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

module.exports = admin;
```

`serviceAccountKey.json`
```json
{
  "type": "service_account",
  "project_id": "classmgmt-aa87d",
  "private_key_id": "6284ed185a40ed4a033b65e82b0d381207686012",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFA=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@classmgmt-aa87d.iam.gserviceaccount.com",
  "client_id": "114230209197125003375",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40classmgmt-aa87d.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

`app.js`
```js
const express = require('express');
const bodyParser = require('body-parser');
const admin = require('./firebaseAdmin');

const cors = require('cors');

const dotenv = require('dotenv');
require('dotenv').config();


const app = express();
app.use(bodyParser.json());
app.use(cors());


async function verifyToken(req, res, next) {
    const idToken = req.headers.authorization;

    if(!idToken) {
        return res.status(401).send('Unauthorized'); 
    }

    try {
        const decodedToken = await admin.auth().verifyIdToken(idToken);
        req.user = decodedToken;
        next();
    }catch(error) {
        return res.status(401).send('Unauthorized');
    }
}


app.listen(3001, () => {
    console.log('Server is running on port 3001');
});
```

