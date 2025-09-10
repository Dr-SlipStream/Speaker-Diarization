import json
import whisper
from pydub import AudioSegment

# Load diarization output from JSON file
with open("diarization_results.json", "r") as f:
    diarization_results = json.load(f)

# Load Whisper model
whisper_model = whisper.load_model("base")

def transcribe_segment(start, end, speaker, audio_file):
    """Extracts a speaker segment and transcribes it."""
    audio = AudioSegment.from_wav(audio_file)
    segment_audio = audio[start * 1000:end * 1000]  # Convert to milliseconds
    segment_audio.export("temp.wav", format="wav")
    
    transcription = whisper_model.transcribe("temp.wav")
    return transcription["text"].strip()

# Process each diarization segment separately
speaker_transcripts = {}
for segment in diarization_results:
    speaker = segment["speaker"]
    start, end = segment["start"], segment["end"]
    
    transcript = transcribe_segment(start, end, speaker, "processed.wav")
    
    if speaker not in speaker_transcripts:
        speaker_transcripts[speaker] = []
    speaker_transcripts[speaker].append(transcript)

# Format output
final_output = []
for speaker, transcript in speaker_transcripts.items():
    final_output.append(f"[{speaker}] {' '.join(transcript)}")

# Save to text file
with open("final_transcript.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(final_output))

print("\n".join(final_output))
