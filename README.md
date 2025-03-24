# Speaker Diarization

This repository provides a **Speaker Diarization** system using **Whisper** for transcription and **pyannote-audio** for speaker segmentation.

## 📌 Features
- **Speaker Diarization**: Identify and separate speakers in an audio file.
- **Transcription**: Convert speech to text using OpenAI's Whisper model.
- **Environment Variable Support**: Uses `.env` file to securely store the Hugging Face authentication token.
- **Easy Installation**: Install dependencies from `readme_docs/`.

---
## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Dr-SlipStream/Speaker-Diarization.git
cd Speaker-Diarization
```

### 2️⃣ Install Dependencies
Check the `readme_docs/` folder for a detailed dependency installation guide.

**Additionally, install `python-dotenv` for `.env` support:**
```sh
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

---
## 📜 Usage

### 🔹 Running `complete_file.py`
To process an audio file, run:
```sh
python complete_file.py 2p_short.wav
```
Replace `2p_short.wav` with your own audio file.

### 🔹 Running Other Scripts
- `diarization_pyannote.py`: Performs speaker diarization using other files in the folder.
- `single_file.py`: Runs transcription and diarization on a single file.

All scripts automatically use the Hugging Face token from `.env`.

---
## 📂 Documentation
Detailed documentation is available in the `readme_docs/` folder.




