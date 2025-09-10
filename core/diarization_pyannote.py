from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.core import Segment
import json
from dotenv import load_dotenv
import os

# Load the token from .env file
load_dotenv()
AUTH_TOKEN = os.getenv("HF_TOKEN")

if AUTH_TOKEN is None:
    raise ValueError("API Token not found. Please set HF_TOKEN in the .env file.")

# Load the diarization pipeline with authentication
diarization_pipeline = SpeakerDiarization.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=AUTH_TOKEN
)

# Run diarization on the processed audio file
diarization_output = diarization_pipeline("processed.wav")

# Store results in a list
diarization_results = []
for turn, _, speaker in diarization_output.itertracks(yield_label=True):
    diarization_results.append({
        "start": round(turn.start, 2),
        "end": round(turn.end, 2),
        "speaker": speaker
    })

# Save to JSON file
with open("diarization_results.json", "w", encoding="utf-8") as f:
    json.dump(diarization_results, f, indent=4)

print("Diarization results saved to diarization_results.json")
