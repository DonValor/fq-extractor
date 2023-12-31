#!/usr/bin/env python

# Program for extracting the NES rom of Full Quiet in:
# Full Quiet (Steam)

# iNES Header for Full Quiet

HEADER = [b'\x4E\x45\x53\x1A\x20\x00\x42\x08\x00\x00\x70\x09\x00\x00\x00\x00']

# OFFSET for the game's ROM in the sharedassets4.assets file
# v2020.3.44.5531  OFFSET     SIZE             OFFSET     SIZE
OFFSET = [{'PRG': [0x010D80C, 0x80000/
], 'CHA': None}]

if __name__ == '__main__':
    # Read in entire .assets file
    f = open("sharedassets4.assets", "rb")
    try:
        exe = f.read()
    finally:
        f.close()

    for i, game in enumerate(HEADER):
        for section in ['PRG', 'CHA']:
            if OFFSET[i][section]:
                start = OFFSET[i][section][0]
                size = OFFSET[i][section][1]
                end = start + size
                game += exe[start:end]
        out = open("FQ_Xbox_V2-Gold.nes", "wb")
        try:
            out.write(game)
        finally:
            out.close()
