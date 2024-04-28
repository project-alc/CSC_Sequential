#This script generates the logisim circuit file for a given tet and octave range
#, puts all the notes in a ROM storage with 4 bit addresses and 14 bit word size
#, and hooks the roms up to buzzers with "hanging" volume and waveform wires.
#, It is up to the user to paste this file into the .circ file and to 
#, connect the wires to a volume input and waveform input (I used a dmx for waveform).
import sys #needed for command line arguments

# tet = int(sys.argv[1]) #Tones of Equal Temperment from 1st argument to command
# octave = int(sys.argv[2]) #Octaves from 2nd argument to command
#starting_Note = int(sys.argv[3]) #Starting Note in Hz, suggested 55 for A0

tet = 12
octave = 3

#fileN = "{}TET_{}-octaves".format(tet, octave) #file name for new ROM


x_coord_pin = 140 #starting address of ROM
y_coord_pin = 160 #starting address of ROM

x_offset = (480 - 90) + 50
y_offset = (960 - 160) + 50

A_0_Hz = 55 #The first note on a standard 88 key piano


# fo = open(fileN, "w+")

header = '  <circuit name="Synth_{}TET_{}-Octaves">\n'.format(tet, octave)
header += '    <a name="appearance" val="logisim_evolution"/>\n'
header += '    <a name="circuit" val="Synth_{}TET_{}-Octaves"/>\n'
header += '    <a name="circuitnamedboxfixedsize" val="true"/>\n'
header += '    <a name="simulationFrequency" val="2.0"/>\n'
footer = '  </circuit>'

string = ""

for oct in range(octave):
  for note in range(tet):
    string += '    <comp lib="0" loc="({},{})" name="Pin">\n'.format((140 + (x_offset * note)), (160 + (y_offset * oct)))
    string += '      <a name="appearance" val="NewPins"/>\n'
    string += '      <a name="facing" val="south"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="0" loc="({},{})" name="Constant">\n'.format((90 + (x_offset * note)), (960 + (y_offset * oct)))
    string += '      <a name="value" val="0x0"/>\n'
    string += '      <a name="width" val="2"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="1" loc="({},{})" name="XOR Gate">\n'.format((160 + (x_offset * note)), (250 + (y_offset * oct)))
    string += '      <a name="facing" val="south"/>\n'
    string += '      <a name="size" val="30"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="10" loc="({},{})" name="Buzzer">\n'.format((270 + (x_offset * note)), (520 + (y_offset * oct)))
    string += '      <a name="facing" val="south"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="10" loc="({},{})" name="Buzzer">\n'.format((310 + (x_offset * note)), (500 + (y_offset * oct)))
    string += '      <a name="facing" val="south"/>\n'
    string += '      <a name="waveform" val="Square"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="10" loc="({},{})" name="Buzzer">\n'.format((350 + (x_offset * note)), (480 + (y_offset * oct)))
    string += '      <a name="facing" val="south"/>\n'
    string += '      <a name="waveform" val="Triangle"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="10" loc="({},{})" name="Buzzer">\n'.format((390 + (x_offset * note)), (460 + (y_offset * oct)))
    string += '      <a name="facing" val="south"/>\n'
    string += '      <a name="waveform" val="Sawtooth"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="2" loc="({},{})" name="Demultiplexer">\n'.format((190 + (x_offset * note)), (560 + (y_offset * oct)))
    string += '      <a name="select" val="2"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="4" loc="({},{})" name="ROM">\n'.format((170 + (x_offset * note)), (600 + (y_offset * oct)))
    string += '      <a name="addrWidth" val="4"/>\n'
    string += '      <a name="appearance" val="logisim_evolution"/>\n'
    string += '      <a name="contents">addr/data: 4 14\n'
    # string += '{}\n'.format(hex(round(A_0_Hz * (2 ** ((note / tet) + oct))))[2:])
    center_Note = A_0_Hz * (2 ** ((note / tet) + oct))
    for k in range(2 ** 3):
      string += '{} '.format(hex(round(center_Note * (2 ** (((k - 8) / (tet*2))))))[2:])
    for k in range(2 ** 3):
      string += '{} '.format(hex(round(center_Note * (2 ** ((k / (tet*2))))))[2:])
    string += '\n</a>\n'
    string += '      <a name="dataWidth" val="14"/>\n'
    string += '    </comp>\n'
    string += '    <comp lib="5" loc="({},{})" name="Button">\n'.format((180 + (x_offset * note)), (140 + (y_offset * oct)))
    string += '      <a name="facing" val="south"/>\n'
    string += '    </comp>\n'
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((100 + (x_offset * note)), (280 + (y_offset * oct)), (100 + (x_offset * note)), (290 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((100 + (x_offset * note)), (290 + (y_offset * oct)), (100 + (x_offset * note)), (590 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((100 + (x_offset * note)), (290 + (y_offset * oct)), (110 + (x_offset * note)), (290 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((100 + (x_offset * note)), (590 + (y_offset * oct)), (210 + (x_offset * note)), (590 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((140 + (x_offset * note)), (160 + (y_offset * oct)), (140 + (x_offset * note)), (200 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((140 + (x_offset * note)), (200 + (y_offset * oct)), (150 + (x_offset * note)), (200 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((150 + (x_offset * note)), (200 + (y_offset * oct)), (150 + (x_offset * note)), (210 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((160 + (x_offset * note)), (250 + (y_offset * oct)), (160 + (x_offset * note)), (560 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((160 + (x_offset * note)), (560 + (y_offset * oct)), (190 + (x_offset * note)), (560 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((170 + (x_offset * note)), (200 + (y_offset * oct)), (170 + (x_offset * note)), (210 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((170 + (x_offset * note)), (200 + (y_offset * oct)), (180 + (x_offset * note)), (200 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((180 + (x_offset * note)), (140 + (y_offset * oct)), (180 + (x_offset * note)), (200 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((210 + (x_offset * note)), (580 + (y_offset * oct)), (210 + (x_offset * note)), (590 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((230 + (x_offset * note)), (540 + (y_offset * oct)), (270 + (x_offset * note)), (540 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((230 + (x_offset * note)), (550 + (y_offset * oct)), (310 + (x_offset * note)), (550 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((230 + (x_offset * note)), (560 + (y_offset * oct)), (350 + (x_offset * note)), (560 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((230 + (x_offset * note)), (570 + (y_offset * oct)), (390 + (x_offset * note)), (570 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((260 + (x_offset * note)), (520 + (y_offset * oct)), (260 + (x_offset * note)), (530 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((260 + (x_offset * note)), (530 + (y_offset * oct)), (400 + (x_offset * note)), (530 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((270 + (x_offset * note)), (520 + (y_offset * oct)), (270 + (x_offset * note)), (540 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((280 + (x_offset * note)), (490 + (y_offset * oct)), (280 + (x_offset * note)), (520 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((280 + (x_offset * note)), (490 + (y_offset * oct)), (320 + (x_offset * note)), (490 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((300 + (x_offset * note)), (500 + (y_offset * oct)), (300 + (x_offset * note)), (520 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((300 + (x_offset * note)), (520 + (y_offset * oct)), (410 + (x_offset * note)), (520 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((310 + (x_offset * note)), (500 + (y_offset * oct)), (310 + (x_offset * note)), (550 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((320 + (x_offset * note)), (490 + (y_offset * oct)), (320 + (x_offset * note)), (500 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((320 + (x_offset * note)), (490 + (y_offset * oct)), (440 + (x_offset * note)), (490 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((340 + (x_offset * note)), (480 + (y_offset * oct)), (340 + (x_offset * note)), (510 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((340 + (x_offset * note)), (510 + (y_offset * oct)), (420 + (x_offset * note)), (510 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((350 + (x_offset * note)), (480 + (y_offset * oct)), (350 + (x_offset * note)), (560 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((360 + (x_offset * note)), (480 + (y_offset * oct)), (440 + (x_offset * note)), (480 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((380 + (x_offset * note)), (460 + (y_offset * oct)), (380 + (x_offset * note)), (500 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((380 + (x_offset * note)), (500 + (y_offset * oct)), (430 + (x_offset * note)), (500 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((390 + (x_offset * note)), (460 + (y_offset * oct)), (390 + (x_offset * note)), (570 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((400 + (x_offset * note)), (460 + (y_offset * oct)), (450 + (x_offset * note)), (460 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((400 + (x_offset * note)), (530 + (y_offset * oct)), (400 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((400 + (x_offset * note)), (580 + (y_offset * oct)), (410 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((410 + (x_offset * note)), (520 + (y_offset * oct)), (410 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((410 + (x_offset * note)), (580 + (y_offset * oct)), (420 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((410 + (x_offset * note)), (660 + (y_offset * oct)), (420 + (x_offset * note)), (660 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((420 + (x_offset * note)), (510 + (y_offset * oct)), (420 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((420 + (x_offset * note)), (580 + (y_offset * oct)), (420 + (x_offset * note)), (660 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((420 + (x_offset * note)), (580 + (y_offset * oct)), (430 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((430 + (x_offset * note)), (500 + (y_offset * oct)), (430 + (x_offset * note)), (580 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((440 + (x_offset * note)), (480 + (y_offset * oct)), (440 + (x_offset * note)), (490 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((440 + (x_offset * note)), (480 + (y_offset * oct)), (450 + (x_offset * note)), (480 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((450 + (x_offset * note)), (460 + (y_offset * oct)), (450 + (x_offset * note)), (480 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((450 + (x_offset * note)), (460 + (y_offset * oct)), (470 + (x_offset * note)), (460 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((460 + (x_offset * note)), (380 + (y_offset * oct)), (470 + (x_offset * note)), (380 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((470 + (x_offset * note)), (370 + (y_offset * oct)), (470 + (x_offset * note)), (380 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((470 + (x_offset * note)), (380 + (y_offset * oct)), (470 + (x_offset * note)), (460 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((470 + (x_offset * note)), (380 + (y_offset * oct)), (480 + (x_offset * note)), (380 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((90 + (x_offset * note)), (290 + (y_offset * oct)), (100 + (x_offset * note)), (290 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((90 + (x_offset * note)), (610 + (y_offset * oct)), (170 + (x_offset * note)), (610 + (y_offset * oct)))
    string += '    <wire from="({},{})" to="({},{})"/>\n'.format((90 + (x_offset * note)), (610 + (y_offset * oct)), (90 + (x_offset * note)), (960 + (y_offset * oct)))
#     freqHex = hex(round(A_0_Hz * (2 ** (note / tet))))[2:]
#     while(len(freqHex) != 4):
#         freqHex = "0" + freqHex
#
#     if ((note % 16) == 0):
#         #print(address)
#         newAddress = hex(address)[2:]
#         while (len(newAddress) != 4):
#             newAddress = "0" + newAddress
#         string += "\n{}: {}".format(newAddress, freqHe + x)
#         address += 0X0010
#     else:
#         string += " {}".format(freqHe + x)
#
# n = 0
# while ( ((tet*octave + n) % 16) != 0):
#     string += " 0000"
#     n += 1
#
# while (address != 0X4000):
#     newAddress = hex(address)[2:]
#     while (len(newAddress) != 4):
#         newAddress = "0" + newAddress
#     string += "\n{}: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000".format(newAddres + s)
#     address += 0X0010
#
#
# #print(file)
# #print(string)
# fo.write(string)
# fo.close()
# print("Saved contents in {}".format(fileN))
write = header + string + footer
print(write)
