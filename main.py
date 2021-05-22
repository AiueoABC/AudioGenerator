import numpy as np  # install : conda install numpy
import pyaudio      # install : conda install pyaudio

SAMPLE_RATE = 44100


# sin Wave Generation and Play
def play(s: pyaudio.Stream, freq: float, duration: float):
    # Generate sin Wave
    samples = np.sin(np.arange(int(duration * SAMPLE_RATE)) * freq * np.pi * 2 / SAMPLE_RATE)
    # Play that
    s.write(samples.astype(np.float32).tostring())
# PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLE_RATE,
                frames_per_buffer=1024,
                output=True)
# ドミソドーを再生
play(stream, 261.626, 0.3)  # note#60 C4
play(stream, 329.628, 0.3)  # note#64 E4
play(stream, 391.995, 0.3)  # note#67 G4
play(stream, 523.251, 0.6)  # note#72 C5
# ストリームを閉じる
stream.close()
# PyAudio終了
p.terminate()