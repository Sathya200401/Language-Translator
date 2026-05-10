# LinguaX - Language Translator

LinguaX is an Android application that provides quick and easy translations across multiple languages. It currently supports a mock translation engine with common travel phrases in 8 languages including Telugu, Spanish, French, Japanese, German, Italian, Hindi, and Korean.

## Setup Instructions

Follow these steps to set up the project locally in Android Studio and run it on your device/emulator.

### 1. Prerequisites
- **Android Studio**: Make sure you have the latest stable version of Android Studio installed (Iguana, Hedgehog, or Giraffe).
- **Java Development Kit (JDK)**: The project uses JDK 17 (Android Studio bundles this by default).

### 2. Opening the Project
1. Open Android Studio.
2. Click on **Open** (or **File > Open** if you are already in another project).
3. Navigate to the directory where you extracted or cloned this project.
4. Select the project folder and click **OK**.
5. Wait for Android Studio to sync the Gradle files. The progress will be shown in the bottom right corner. 

*(If you see any "Sync Failed" messages, ensure you have an active internet connection so Gradle can download the necessary dependencies like `androidx.core`, `androidx.navigation`, and `com.airbnb.android:lottie`).*

### 3. Setting Up a Device (Emulator or Physical)
To test the app, you need a device to run it on.

**Option A: Using an Android Emulator (Virtual Device)**
1. In Android Studio, look at the top toolbar and find the **Device Manager** icon (it looks like a small phone with an Android logo).
2. Click **Create Device**.
3. Select a hardware profile (e.g., Pixel 7) and click **Next**.
4. Choose a System Image (API Level 34 is recommended since the `targetSdk` is 34). If you don't have it downloaded, click the small download icon next to it.
5. Click **Next**, name your emulator, and click **Finish**.
6. Click the "Play" icon next to the emulator in the Device Manager to launch it.

**Option B: Using a Physical Android Device**
1. On your physical Android phone, go to **Settings > About Phone**.
2. Tap on **Build Number** 7 times until you see a message saying "You are now a developer!".
3. Go back to Settings and open **Developer Options**.
4. Enable **USB Debugging**.
5. Connect your phone to your computer via a USB cable. 
6. Allow the debugging prompt on your phone's screen.
7. Your device should now appear in the device dropdown menu in Android Studio's top toolbar.

### 4. Running the App
1. In the top toolbar of Android Studio, ensure `app` is selected in the Run Configurations dropdown.
2. Next to it, ensure your emulator or physical device is selected.
3. Click the green **Run (Play)** button (or press `Shift + F10`).
4. Android Studio will build the APK and install it on your device. Once installed, LinguaX will open automatically.

### 5. Testing the Screens
Once the app is running:
- **Splash Screen**: You should briefly see a modern splash screen before it navigates to the Home screen.
- **Home Screen**: 
  - **Change Target Language**: Tap on the target language (e.g., 🇮🇳 Telugu) to cycle through the available languages (Spanish, French, Japanese, German, Italian, Hindi, Korean).
  - **Translate**: Type one of the supported mock phrases (e.g., "how are you?") and click **Translate**.
  - **Copy to Clipboard**: After a translation appears, click the small copy icon in the bottom right corner of the translation box to copy the text. A toast message should appear.

---

## Project Structure

- **`app/build.gradle`**: 
  - The `targetSdk` and `compileSdk` are set to 34 (Android 14).
  - Contains necessary dependencies (`navigation-fragment`, `lottie`, `material`).
  - ViewBinding is enabled.
- **`AndroidManifest.xml`**:
  - `MainActivity` is exported and set as the Launcher activity.
  - The App Theme is properly linked.
- **`strings.xml`**: String resources for `app_name` and `subtitle` are defined here.

## Future Enhancements

If you decide to integrate a real Translation API (like Google ML Kit) in the future, you will need to add the ML Kit translation dependency to `app/build.gradle` and potentially the `INTERNET` permission to `AndroidManifest.xml`. For now, the offline mock setup works perfectly!
