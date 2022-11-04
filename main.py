import noteGenerator

ng = noteGenerator.NoteGenerator()

# open note generator
ng.open()

# Play note
# ng.play_hz(261.626, 0.3)  # note#60 C4
# ng.play_hz(329.628, 0.3)  # note#64 E4
# ng.play_hz(391.995, 0.3)  # note#67 G4
# ng.play_hz(523.251, 0.6)  # note#72 C5
ng.play_tone('C4', 0.3)  # note#60 C4
ng.play_tone('E4', 0.3)  # note#64 E4
ng.play_tone('G4', 0.3)  # note#67 G4
ng.play_tone('C5', 0.6)  # note#72 C5

# close note generator
ng.close()