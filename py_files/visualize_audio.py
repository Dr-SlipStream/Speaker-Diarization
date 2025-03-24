import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load the processed audio file
y, sr = librosa.load("processed.wav", sr=16000)

# Plot waveform
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform of Processed Audio")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
