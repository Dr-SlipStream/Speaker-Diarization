# Speaker Diarization

This repository provides a **Speaker Diarization** system using **Whisper** for transcription and **pyannote-audio** for speaker segmentation.

## 📌 Features
- **Speaker Diarization**: Identify and separate speakers in an audio file.
- **Transcription**: Convert speech to text using OpenAI's Whisper model.
- **Environment Variable Support**: Uses `.env` file to securely store the Hugging Face authentication token.
- **Single-Step Processing**: Run a single script to process audio and generate a speaker-labeled transcript.
- **Streamlit Dashboard**: Provides a user-friendly interface for uploading and processing audio files.

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

#### **Set Up a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows
```

#### **Install Required Packages**
```sh
pip install -r requirements.txt
pip install python-dotenv streamlit
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
## 🐛 Usage

### 🔹 Running `complete_file.py`
To process an audio file, run:
```sh
python complete_file.py <audio_file>
```
Replace `<audio_file>` with your actual file.

### 🔹 Running the Streamlit Dashboard
To start the Streamlit app locally:
```sh
streamlit run app.py
```
This launches a web interface where you can upload audio files and view transcripts.

### 🔹 Output
- The final transcript is saved as:
```sh
<audio_file_name>_transcript.txt
```
- In the Streamlit app, transcripts can be viewed and downloaded.

---
## 📂 Documentation
Detailed documentation is available in the `readme_docs/` folder.

---
## 📈 Deploying on Streamlit Cloud
To deploy on **Streamlit Cloud**:

1. **Push to GitHub**
```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```
2. **Go to [Streamlit Cloud](https://share.streamlit.io/)** and log in.
3. Click **New app** and select your repository.
4. Set `app.py` as the entry point.
5. Click **Deploy**.

Your application will now be live, allowing users to upload and process audio files via a web interface. 🚀

