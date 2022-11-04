import numpy as np
import pyaudio


class NoteGenerator:
    def __init__(self, sample_rate: int = 44100):
        self.stream = None
        self.p = None
        # set sample rate
        self.sample_rate = sample_rate

    def open(self):
        # PyAudio
        self.p = pyaudio.PyAudio() if self.p is None else self.p
        # open stream
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            frames_per_buffer=1024,
            output=True
        ) if self.stream is None else self.stream

    # sin Wave Generation and Play
    def play_hz(self, freq: float, duration: float):
        if self.stream is None:
            return False
        else:
            # Generate sin Wave
            samples = np.sin(np.arange(int(duration * self.sample_rate)) * freq * np.pi * 2 / self.sample_rate)
            # Play that
            self.stream.write(samples.astype(np.float32).tostring())
            return True

    def play_tone(self, note, duration):
        self.play_hz(_note2hz(note), duration)

    def close(self):
        # close stream
        self.stream.close()
        # close PyAudio
        self.p.terminate()
        self.stream = None
        self.p = None


def _note2hz(note: str):
    # find key number, #49 is A4 and 440 Hz
    # And generate Hz
    key = 0
    note = note.upper()
    code1 = note[0]
    if len(note) == 2:
        try:
            if code1 == 'A':
                key = 12 * int(note[1]) + 1
            elif code1 == 'B':
                key = 12 * int(note[1]) + 3
            elif code1 == 'C':
                key = 12 * int(note[1]) - 8
            elif code1 == 'D':
                key = 12 * int(note[1]) - 6
            elif code1 == 'E':
                key = 12 * int(note[1]) - 4
            elif code1 == 'F':
                key = 12 * int(note[1]) - 3
            elif code1 == 'G':
                key = 12 * int(note[1]) - 1
        except:
            print('note should be 2~3 length string, like A4, A#4')
            return 0.
    elif len(note) == 3:
        try:
            if code1 == 'A':
                key = 12 * int(note[2]) + 2
            elif code1 == 'C':
                key = 12 * int(note[2]) - 7
            elif code1 == 'D':
                key = 12 * int(note[2]) - 5
            elif code1 == 'F':
                key = 12 * int(note[2]) - 2
            elif code1 == 'G':
                key = 12 * int(note[2])
        except:
            print('note should be 2~3 length string, like A4, A#4')
            return 0.
    else:
        print('note should be 2~3 length string, like A4, A#4')
        return 0.

    # r = 2^(1/12) = 1.0594630943592953, a(49) = 440 = a(0) * r^49 => a(0) = 25.956543598746517
    return 25.956543598746517 * 1.0594630943592953 ** key