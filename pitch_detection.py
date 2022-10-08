import statistics as sts
import math

file_name = 'Song_for_Ellen.txt'
with open('P_{}'.format(file_name), 'r') as f:
    file_reader = f.readlines()

#write into lines, line [time][freq(4200)]
lines = []
for line in file_reader:
    line = line.strip()
    line = line.split(',')
    line = [int(num) for num in line]
    lines.append(line)

#find frequencies with significantly high amplitudes
#and store them in a dictionary
#where the key is time and the value is of type list
sig_freq = {}
for time, line in enumerate(lines):
    threshhold = sts.fmean(line) + 4*sts.stdev(line) #NOTE stdev may change
    freqs = []
    for index, value in enumerate(line):
        if value > threshhold:
            freqs.append(index)  
    sig_freq[time] = freqs


#converting frequencies into the nth keys on a standard piano
#A4 is 440Hz at the 49th key on an 88-key piano 
keys = {}
for i in sig_freq:
    key_numbers = set()
    for freq in sig_freq[i]:
        key_numbers.add(round(12*math.log2(freq/440.0)+49))
    keys[i] = key_numbers


#get notes depending on which keys there are
notes = {}
for i in keys:
    note = set()
    for key in keys[i]:
        if (key % 12 == 1):
            note.add("A")
        elif (key % 12 == 2):
            note.add("b")
        elif (key % 12 == 3):
            note.add("B")
        elif (key % 12 == 4):
            note.add("C")
        elif (key % 12 == 5):
            note.add("d")
        elif (key % 12 == 6):
            note.add("D")
        elif (key % 12 == 7):
            note.add("e")
        elif (key % 12 == 8):
            note.add("E")
        elif (key % 12 == 9):
            note.add("F")
        elif (key % 12 == 10):
            note.add("g")
        elif (key % 12 == 11):
            note.add("G")
        elif (key % 12 == 0):
            note.add("a")
        # else:
        #     note.add("N")
    notes[i] = note


#this is an extra step for later use of Processing
total_num_of_notes = 0
for i in notes:
    total_num_of_notes += len(notes[i])

print(total_num_of_notes)

with open("N_{}.csv".format(file_name[:-4]), 'w') as f:
    f.write(str(total_num_of_notes)+',\n')
    for i in notes:
        for note in notes[i]:
            f.write(str(i)+',')
            f.write(note)
            f.write('\n')

