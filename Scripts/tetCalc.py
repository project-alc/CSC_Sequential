#This script generates a ROM file that has all the notes starting with A0 to AN
#Where N is the nth octave desired in a desired Temperment system.
#Usage is:
#   python tetCalc.py tet octave
#A file will be written with a descriptive name
import sys #needed for command line arguments

# tet = int(sys.argv[1]) #Tones of Equal Temperment from 1st argument to command
# octave = int(sys.argv[2]) #Octaves from 2nd argument to command
tet = 12
octave = 2

fileN = "{}TET_{}-octaves".format(tet, octave) #file name for new ROM


address = 0X0000 #starting address of ROM

A_0_Hz = 55 #The first note on a standard 88 key piano

starting_note = A_0_Hz * (2 ** 3)

fo = open(fileN, "w+")

string = "v3.0 hex words addressed"

for note in range(tet*octave):
    # freqHex = hex(round(A_0_Hz * (2 ** (note / tet))))[2:]
    freqHex = hex(round(starting_note * (2 ** (note / tet))))[2:]
    while(len(freqHex) != 4):
        freqHex = "0" + freqHex

    if ((note % 16) == 0):
        #print(address)
        newAddress = hex(address)[2:]
        while (len(newAddress) != 4):
            newAddress = "0" + newAddress
        string += "\n{}: {}".format(newAddress, freqHex)
        address += 0X0010
    else:
        string += " {}".format(freqHex)

n = 0
while ( ((tet*octave + n) % 16) != 0):
    string += " 0000"
    n += 1

while (address != 0X4000):
    newAddress = hex(address)[2:]
    while (len(newAddress) != 4):
        newAddress = "0" + newAddress
    string += "\n{}: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000".format(newAddress)
    address += 0X0010


#print(file)
#print(string)
fo.write(string)
fo.close()
print("Saved contents in {}".format(fileN))
