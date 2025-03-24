from pydub import AudioSegment

# Load the audio file (change 'input.wav' if needed)
audio = AudioSegment.from_file("2p_short.wav")

# Convert to 16kHz
audio = audio.set_frame_rate(16000)

# Export processed audio
audio.export("processed.wav", format="wav")

print("Audio successfully converted to 16kHz and saved as 'processed.wav'!")