import wave
import matplotlib.pyplot as plt
import numpy as np
import pyaudio

# Loading audio file
filename = 'data/Loc1V1.wav'
wf = wave.open(filename, 'rb')

# ---------- DISPLAY DATA ----------

# Retrieve parameters
# n_channels = wf.getnchannels()
# sample_width = wf.getsampwidth()
# framerate = wf.getframerate()
# n_frames = wf.getnframes()
#
# # Data extraction
# signal = wf.readframes(n_frames)
# signal = np.frombuffer(signal, dtype=np.int16)
#
# # Plot signal
# plt.figure()
# plt.plot(signal)
# plt.title('Audio Signal Loc1V1')
# plt.xlabel('Samples')
# plt.ylabel('Amplitude')
# plt.show()

# ---------- STREAMING DATA ----------

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream to play audio
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# Read and play audio in chunks
chunk = 1024
data = wf.readframes(chunk)

while data:
    stream.write(data)
    data = wf.readframes(chunk)

# Close the stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()