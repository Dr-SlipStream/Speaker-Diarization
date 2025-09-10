import whisper

# Load Whisper ASR model
model = whisper.load_model("base")

# Transcribe the processed audio
result = model.transcribe("processed.wav")

# Print and save the transcript
print("Transcription:\n", result["text"])

with open("whisper_transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Whisper transcription saved to whisper_transcript.txt")
