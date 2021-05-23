import numpy as np
import pyaudio
import noteGenerator as ng

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
# Play note
play(stream, ng.note2Hz('C4'), 0.3)  # C4
play(stream, ng.note2Hz('E4'), 0.3)  # E4
play(stream, ng.note2Hz('G4'), 0.3)  # G4
play(stream, ng.note2Hz('C5'), 0.6)  # C5

play(stream, ng.note2Hz('C5'), 0.6)  # C5
play(stream, ng.note2Hz('G4'), 0.3)  # G4
play(stream, ng.note2Hz('E4'), 0.3)  # E4
play(stream, ng.note2Hz('C4'), 0.3)  # C4

# close stream
stream.close()
# close PyAudio
p.terminate()
