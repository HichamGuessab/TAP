import wave
import matplotlib.pyplot as plt
import numpy as np

# Loading audio file
filename = 'data/Loc1V1.wav'
wf = wave.open(filename, 'rb')

# Retrieve parameters
n_channels = wf.getnchannels()
sample_width = wf.getsampwidth()
framerate = wf.getframerate()
n_frames = wf.getnframes()

# Data extraction
signal = wf.readframes(n_frames)
signal = np.frombuffer(signal, dtype=np.int16)

# Plot signal
plt.figure()
plt.plot(signal)
plt.title('Audio Signal Loc1V1')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.show()