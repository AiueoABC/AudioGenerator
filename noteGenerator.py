def note2Hz(note:str):
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