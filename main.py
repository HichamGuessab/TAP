import wave
import matplotlib.pyplot as plt
import numpy as np
import pyaudio

def load_audio(filename):
    wave_read = wave.open(filename, 'rb')
    frames = wave_read.readframes(wave_read.getnframes())
    signal = np.frombuffer(frames, dtype=np.int16)
    return signal, wave_read

def display_waveform(signal):
    plt.figure()
    plt.plot(signal)
    plt.title('Audio Signal')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.show()

def stream_audio(wave_read):
    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=p.get_format_from_width(wave_read.getsampwidth()),
                        channels=wave_read.getnchannels(),
                        rate=wave_read.getframerate(),
                        output=True)

        wave_read.rewind()
        chunk = 1024
        data = wave_read.readframes(chunk)

        while data:
            stream.write(data)
            data = wave_read.readframes(chunk)

        stream.stop_stream()
        stream.close()
    finally:
        p.terminate()

if __name__ == "__main__":
    filename = 'data/Loc1V1.wav'
    wave_read = wave.open(filename, 'rb')

    signal_1, wave_read_1 = load_audio('data/Loc1V1.wav')
    signal_2, wave_read_2 = load_audio('data/Loc1V2.wav')

    display_waveform(signal_1)
    stream_audio(wave_read)
