**“Create a complete note covering every step we followed to convert my React portfolio into an APK using Capacitor, including icon setup and installation. Everything should be documented clearly.”**

Good. I’ll write this as a clean technical note you can store for future reference.

---

# React Portfolio → Android APK using Capacitor

Complete CLI-Based Workflow (No Android Studio UI)

---

## 1. Project Context

We started with:

• A frontend-only React portfolio website
• Built using `npm run build`
• Goal: Convert it into an Android APK
• Constraint: No Android Studio GUI usage

---

# 2. Installing Capacitor

Inside the React project root:

```bash
npm install @capacitor/core @capacitor/cli
```

Initialize Capacitor:

```bash
npx cap init
```

It asks:

* App Name → Your app display name
* App ID → Example: com.shudarsan.portfolio

App ID must follow reverse domain format.

---

# 3. Build React App

```bash
npm run build
```

This generates:

```
build/
```

That folder contains your production frontend files.

---

# 4. Configure Capacitor

Open:

```
capacitor.config.ts
```

Set:

```ts
webDir: 'build'
```

This tells Capacitor where your frontend build exists.

---

# 5. Add Android Platform

```bash
npx cap add android
```

This creates:

```
android/
```

Now your web app is wrapped inside a native Android project.

---

# 6. Sync After Every Build

Whenever you change frontend code:

```bash
npm run build
npx cap copy
```

or

```bash
npx cap sync
```

This pushes updated files into the Android project.

---

# 7. Fixing SDK Location Error

If this error appears:

```
SDK location not found
```

It means Gradle does not know where Android SDK is.

Since SDK was located at:

```
/home/aparichit/Android/Sdk
```

We created:

```
android/local.properties
```

Inside it:

```
sdk.dir=/home/aparichit/Android/Sdk
```

Important:

* Use full absolute path
* Do not use ~

---

# 8. Build APK Using CLI Only

Inside android folder:

```bash
cd android
./gradlew assembleDebug
```

If permission error:

```bash
chmod +x gradlew
```

After successful build, APK location:

```
android/app/build/outputs/apk/debug/app-debug.apk
```

This is your installable debug APK.

---

# 9. Installing APK on Phone

Enable:

• Developer Options
• USB Debugging

Check device:

```bash
adb devices
```

If it shows:

```
unauthorized
```

Fix:

• Unlock phone
• Accept “Allow USB debugging” popup
• Or revoke USB debugging authorization and reconnect

When device shows:

```
device
```

Install app:

```bash
adb install app-debug.apk
```

If already installed:

```bash
adb install -r app-debug.apk
```

`-r` means replace existing app.

---

# 10. Changing App Icon

Default Android icons are inside:

```
android/app/src/main/res/
```

Folders:

```
mipmap-mdpi
mipmap-hdpi
mipmap-xhdpi
mipmap-xxhdpi
mipmap-xxxhdpi
```

Each contains:

```
ic_launcher.png
```

Instead of manually resizing, we used an automated tool.

---

## Recommended Method: capacitor-assets

Install globally:

```bash
npm install -g @capacitor/assets
```

Inside project root, create:

```
assets/icon.png
```

Use:

• Square image
• Recommended 1024x1024
• Transparent background preferred

Generate icons:

```bash
npx capacitor-assets generate --android
```

Then sync:

```bash
npx cap sync
```

Rebuild:

```bash
cd android
./gradlew assembleDebug
```

Then reinstall app.

If icon does not update:
Uninstall old app and install again.

Android sometimes caches icons.

---

# 11. Full Flow Summary

Frontend Build
→ Capacitor Wrap
→ Android Project
→ Gradle Build
→ APK Generated
→ ADB Install

No Android Studio UI involved.

---
