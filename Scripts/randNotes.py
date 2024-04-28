#This script generates a ROM file that contains randomly generated notes in a given
#tet and octave range for the "Ear Training" game. 
#Two files are generated, one with the notes themselves, and the other with the interval between
#those notes. To make things easier, the notes come in pairs of two random notes within an
#octave range, inclusively, and the intervals come in pairs of the same intervals.
#E.G. If the notes 1B8 and 2BA were chosen (A3 and F3 in hex), then
# the interval ROM would have 8 and 8. The reason for this
#is that all the notes come in ascending pairs, but the interval game allows for decending
#intervals, so if the game choses an even address in rom, then you would get A up to F as
#the question, with an answer of 8 steps ascending, and if the game chose an odd address (descending),
#Then you would get F down to A which has the answer of 8 steps desceding.
import sys #needed for command line arguments
from random import randrange
# tet = int(sys.argv[1]) #Tones of Equal Temperment from 1st argument to command
# octave = int(sys.argv[2]) #Octaves from 2nd argument to command
memory_bits = 14

tet = 12

octave = 3

file1 = "{}TET_{}-octaves_Rand_NOTES".format(tet, octave) #file name for new ROM
file2 = "{}TET_{}-octaves_Rand_INTERVALS".format(tet, octave) #file name for new ROM


address = 0X0000 #starting address of ROM

# A_0_Hz = 55 #The first note on a standard 88 key piano
A_4_Hz = 440 #The orchestra note

notes = []
# interval = []
# note_pairs = []

for note in range(tet*octave):
    freqHex = hex(round(A_4_Hz * (2 ** (note / tet))))[2:]
    while(len(freqHex) != 4):
        freqHex = "0" + freqHex

    notes.append(freqHex)

# print(*notes)

string1 = "v3.0 hex words addressed"
string2 = "v3.0 hex words addressed"

for pair in range(2 ** (memory_bits - 1) ):
    note1 = randrange(len(notes))
    note2 = randrange(13)
    if ( (note1 + note2) >=  len(notes) ):
        temp = note1
        note1 = note1 - note2
        note2 = temp
    else:
        note2 = note1 + note2
    interval = hex(note2 - note1)[2:]
    while (len(interval) != 4):
            interval = "0" + interval
    # note_pairs.append(notes[note1])
    # note_pairs.append( notes[note2])
    # interval.append(note2 - note1)
    # interval.append(note2 - note1)
    if ((pair % 8) == 0):
        #print(address)
        newAddress = hex(address)[2:]
        while (len(newAddress) != 4):
            newAddress = "0" + newAddress
        string1 += "\n{}: {} {}".format(newAddress, notes[note1], notes[note2])
        string2 += "\n{}: {} {}".format(newAddress, interval, interval)
        address += 0X0010
    else:
        string1 += " {} {}".format(notes[note1], notes[note2])
        string2 += " {} {}".format(interval, interval)

fo1 = open(file1, "w+")
fo1.write(string1)
fo1.close()

fo2 = open(file2, "w+")
fo2.write(string2)
fo2.close()
# #print(file)
# #print(string)
print("Saved notes in {} and intervals in {} which can be loaded into a LogiSim ROM module".format(file1, file2))
