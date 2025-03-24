# Speaker Diarization

This repository provides a **Speaker Diarization** system using **Whisper** for transcription and **pyannote-audio** for speaker segmentation.

## 📌 Features
- **Speaker Diarization**: Identify and separate speakers in an audio file.
- **Transcription**: Convert speech to text using OpenAI's Whisper model.
- **Environment Variable Support**: Uses `.env` file to securely store the Hugging Face authentication token.
- **Single-Step Processing**: Run a single script to process audio and generate a speaker-labeled transcript.

---
## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Dr-SlipStream/Speaker-Diarization.git
cd Speaker-Diarization
```

### 2️⃣ Install Dependencies
Ensure Python 3.11.x (preferably 3.11.9) is installed.

#### **Check Python Version**
```sh
python --version
```
If another version is installed, uninstall it and install Python 3.11.9.

#### **Install Required Packages**
```sh
pip install -r requirements.txt
pip install python-dotenv
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory:
```sh
touch .env
```
Edit `.env` and add your Hugging Face token:
```sh
HF_TOKEN=your_hugging_face_token_here
```

To get a Hugging Face token:
1. Go to [Hugging Face](https://huggingface.co/)
2. Sign in and navigate to your profile settings.
3. Generate an API token under 'Access Tokens'.

---
## 📜 Usage

### 🔹 Running `complete_file.py`
To process an audio file, run:
```sh
python complete_file.py <audio_file>
```
Replace `<audio_file>` with your actual file.

### 🔹 Output
The final transcript is saved as:
```sh
<audio_file_name>_transcript.txt
```

---
## 📂 Documentation
Detailed documentation is available in the `readme_docs/` folder.

