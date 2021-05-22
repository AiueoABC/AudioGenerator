import numpy as np  # install : conda install numpy
import pyaudio      # install : conda install pyaudio
import noteGenerator as ng
import PySimpleGUI as sg

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
# Key board generation
layout = [
    [sg.Button('', size=(2, 11)),
     sg.Button('C#', size=(2, 11), button_color='black'),
     sg.Button('', size=(1, 11)),
     sg.Button('D#', size=(2, 11), button_color='black'),
     sg.Button('', size=(2, 11)),
     sg.Button('F#', size=(2, 11), button_color='black'),
     sg.Button('', size=(1, 11)),
     sg.Button('G#', size=(2, 11), button_color='black'),
     sg.Button('', size=(1, 11)),
     sg.Button('A#', size=(2, 11), button_color='black'),
     sg.Button('', size=(2, 11))],
    [sg.Button('C', size=(4, 13), button_color='Gray'),
     sg.Button('D', size=(4, 13), button_color='Gray'),
     sg.Button('E', size=(4, 13), button_color='Gray'),
     sg.Button('F', size=(4, 13), button_color='Gray'),
     sg.Button('G', size=(4, 13), button_color='Gray'),
     sg.Button('A', size=(4, 13), button_color='Gray'),
     sg.Button('B', size=(4, 13), button_color='Gray')]
]
window = sg.Window('Play with DroidCam', layout, location=(600, 200), finalize=True, element_justification='center')
noteLv = 4
wave = 0
while True:
    event, values = window.read(timeout=1)
    if event in (None, 'Exit'):
        break
    elif event != '__TIMEOUT__':
        wave = ng.note2Hz(f'{event}{noteLv}')
    print(wave)
    play(stream, wave, 0.1)
# close stream
stream.close()
# close PyAudio
p.terminate()
# close window
window.close()
