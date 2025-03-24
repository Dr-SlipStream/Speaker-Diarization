import sys
import os
import whisper
import torch
from pydub import AudioSegment
from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.core import Segment
from dotenv import load_dotenv

# Load the token from .env file
load_dotenv()
AUTH_TOKEN = os.getenv("HF_TOKEN")

if AUTH_TOKEN is None:
    raise ValueError("API Token not found. Please set HF_TOKEN in the .env file.")

# Check if input file is provided
if len(sys.argv) < 2:
    print("Usage: python process_audio.py <input_audio_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Check if file exists
if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found!")
    sys.exit(1)

# Convert audio to 16kHz WAV
audio = AudioSegment.from_file(input_file).set_frame_rate(16000)
audio = audio.set_channels(1)  # Ensure mono audio
audio.export("temp.wav", format="wav")

# Run speaker diarization
diarization_pipeline = SpeakerDiarization.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=AUTH_TOKEN
)
diarization_output = diarization_pipeline("temp.wav")

# Load Whisper model
whisper_model = whisper.load_model("base")

# Function to transcribe a segment
def transcribe_segment(start, end):
    """Extract and transcribe a specific audio segment."""
    segment_audio = audio[start * 1000:end * 1000]  # Convert seconds to ms
    segment_audio.export("segment.wav", format="wav")
    return whisper_model.transcribe("segment.wav")["text"].strip()

# Process diarization output
transcript = []
for segment, _, speaker in diarization_output.itertracks(yield_label=True):
    text = transcribe_segment(segment.start, segment.end)
    transcript.append(f"[{speaker}] {text}")

# Final transcript
final_transcript = "\n".join(transcript)
print(final_transcript)

# Save transcript to a text file
output_filename = os.path.splitext(input_file)[0] + "_transcript.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(final_transcript)

print(f"Transcript saved to {output_filename}")

# Clean up temporary files
os.remove("temp.wav")
os.remove("segment.wav")
