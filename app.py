import streamlit as st
import sys
import subprocess
import os
import shutil

# Set the page title
st.set_page_config(page_title="Speaker Diarization & Transcription", layout="wide")

st.title("Speaker Diarization & Transcription")
st.write("Upload an audio file (.wav) to transcribe and label speakers.")

# Ensure the 'uploads' directory exists
UPLOADS_DIR = "uploads"
os.makedirs(UPLOADS_DIR, exist_ok=True)

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])

if uploaded_file is not None:
    # Save the uploaded file
    audio_path = os.path.join(UPLOADS_DIR, uploaded_file.name)

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded: {uploaded_file.name}")

    # Run the script when the user clicks the button
    if st.button("Process Audio"):
        with st.spinner("Processing..."):
            result = subprocess.run([sys.executable, "complete_file.py", audio_path], capture_output=True, text=True)

        if result.returncode == 0:
            st.success("Processing complete! Transcript generated.")

            # Show logs (stdout + stderr)
            logs = (result.stdout or "") + "\n" + (result.stderr or "")
            st.text_area("Logs:", logs, height=200)

            # Get filename without extension
            file_base_name = os.path.splitext(uploaded_file.name)[0]
            transcript_path = os.path.join(UPLOADS_DIR, f"{file_base_name}_transcript.txt")

            if os.path.exists(transcript_path):
                with open(transcript_path, "r") as f:
                    transcript = f.read()
                st.text_area("Transcript:", transcript, height=300)
                st.download_button("Download Transcript", transcript, file_name=f"{file_base_name}_transcript.txt")
            else:
                st.error(f"Transcript file not found at {transcript_path}")
        else:
            st.error("Error processing the file. Check logs below:")
            st.subheader("Error Logs")
            st.text(result.stderr)  # shows the error output from complete_file.py

            # Show logs when error happens
            logs = (result.stdout or "") + "\n" + (result.stderr or "")
            st.text_area("Logs:", logs, height=300)


# Button to clear uploads folder
if st.button("Clear Uploads Folder"):
    with st.spinner("Clearing uploads folder..."):
        for file in os.listdir(UPLOADS_DIR):
            file_path = os.path.join(UPLOADS_DIR, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                st.error(f"Error deleting {file}: {e}")
        st.success("Uploads folder cleared successfully!")
