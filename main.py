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

def extract_middle_segment(signal, wave_read, duration_ms):
    sr = wave_read.getframerate()
    num_samples = int((duration_ms / 1000) * sr)

    start_index = len(signal) // 2 - num_samples // 2
    end_index = start_index + num_samples

    return signal[start_index:end_index], sr

def display_spectrograms(wave_read_1, signal_1, title_1, wave_read_2, signal_2, title_2):
    sr1 = wave_read_1.getframerate()
    sr2 = wave_read_2.getframerate()

    plt.figure(figsize=(12, 6))

    # First subplot
    plt.subplot(1, 2, 1)
    plt.specgram(signal_1, Fs=sr1, scale='dB')
    plt.colorbar(label='Intensity (dB)')
    plt.title(title_1)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

    # Second subplot
    plt.subplot(1, 2, 2)
    plt.specgram(signal_2, Fs=sr2, scale='dB')
    plt.colorbar(label='Intensity (dB)')
    plt.title(title_2)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    loc1V1_signal, loc1V1_wr = load_audio('data/Loc1V1.wav')
    loc1V2_signal, loc1V2_wr = load_audio('data/Loc1V2.wav')
    loc2V1_signal, loc2V1_wr = load_audio('data/Loc2V1.wav')

    print(loc1V1_wr.getparams())
    # _wave_params(nchannels=1, sampwidth=2, framerate=16000, nframes=23021, comptype='NONE', compname='not compressed')

    # display_waveform(signal_1)
    # stream_audio(wave_read)
    # display_spectrograms(loc1V1_wr, loc1V1_signal, "Loc1V1", loc1V2_wr, loc1V2_signal, "Loc1V2")
    # display_spectrograms(loc1V1_wr, loc1V1_signal, "Loc1V1", loc2V1_wr, loc2V1_signal, "Loc2V1")
