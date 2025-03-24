import json
import whisper
import librosa
import librosa.display
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.core import Segment
from dotenv import load_dotenv  # Load .env files
import os  # To access environment variables

# Load the token from .env file
load_dotenv()
AUTH_TOKEN = os.getenv("HF_TOKEN")

if AUTH_TOKEN is None:
    raise ValueError("API Token not found. Please set HF_TOKEN in the .env file.")

# Step 1: Convert Audio
def convert_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(16000)
    audio.export(output_file, format="wav")
    print("Audio successfully converted to 16kHz and saved as", output_file)

# Step 2: Speaker Diarization
def perform_diarization(audio_file, output_json):
    diarization_pipeline = SpeakerDiarization.from_pretrained(
        "pyannote/speaker-diarization", use_auth_token=AUTH_TOKEN
    )
    diarization_output = diarization_pipeline(audio_file)
    diarization_results = []
    for turn, _, speaker in diarization_output.itertracks(yield_label=True):
        diarization_results.append({"start": round(turn.start, 2), "end": round(turn.end, 2), "speaker": speaker})
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(diarization_results, f, indent=4)
    print("Diarization results saved to", output_json)

# Step 3 (Optional): Visualize Audio
def visualize_audio(audio_file):
    y, sr = librosa.load(audio_file, sr=16000)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform of Processed Audio")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

# Step 4: Full Audio Transcription
def transcribe_audio(audio_file, transcript_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("Whisper transcription saved to", transcript_file)
    return result["text"]

# Step 5: Generate Speaker-Wise Transcription
def transcribe_speaker_wise(diarization_json, audio_file, output_file):
    with open(diarization_json, "r") as f:
        diarization_results = json.load(f)
    whisper_model = whisper.load_model("base")
    speaker_transcripts = {}

    for segment in diarization_results:
        speaker = segment["speaker"]
        start, end = segment["start"], segment["end"]
        audio = AudioSegment.from_wav(audio_file)
        segment_audio = audio[start * 1000:end * 1000]
        segment_audio.export("temp.wav", format="wav")
        transcription = whisper_model.transcribe("temp.wav")["text"].strip()
        if speaker not in speaker_transcripts:
            speaker_transcripts[speaker] = []
        speaker_transcripts[speaker].append(transcription)

    final_output = []
    for speaker, transcript in speaker_transcripts.items():
        final_output.append(f"[{speaker}] {' '.join(transcript)}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(final_output))
    print("Speaker-wise transcription saved to", output_file)

# Run all steps sequentially
def main():
    input_audio = "2p_short.wav"
    processed_audio = "processed.wav"
    diarization_json = "diarization_results.json"
    transcript_file = "whisper_transcript.txt"
    final_transcript_file = "final_transcript.txt"

    convert_audio(input_audio, processed_audio)
    perform_diarization(processed_audio, diarization_json)
    visualize_audio(processed_audio)  # Optional visualization
    transcribe_audio(processed_audio, transcript_file)
    transcribe_speaker_wise(diarization_json, processed_audio, final_transcript_file)
    print("All processes completed successfully!")

if __name__ == "__main__":
    main()
