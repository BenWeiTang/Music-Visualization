
file_name = 'Song_for_Ellen.txt'

#read original text file
with open(file_name, 'r') as f:
    file_reader = f.readlines()

#write a parsed version to a new file, freq range from 1-4200 (indices 0-4199)
with open('P_{}'.format(file_name), 'w') as f:
    for i in range(4200):
        f.write(file_reader[i])

#read the parsed file
with open('P_{}'.format(file_name), 'r') as f:
    p_file_reader = f.readlines()

#lines are a list of lists which result from strings in p_file_reader
lines = []
for line in p_file_reader:
    line = line.split(',') #turn a string into a list
    line[-1] = line[-1].strip() #get rid of newline chr at the end
    lines.append(line)

#flip the time axis and freq axis
num_of_freq = len(lines) #should always be 4200 
num_of_sec = len(lines[0]) #every other line will do. this is time in seconds

new_lines = []
for sec in range(num_of_sec):
    new_line = [lines[freq][sec] for freq in range(num_of_freq)]
    new_lines.append(new_line)


# overwrite the fliped lines the P_ file
# for now the colomns represent time and rows represents freq
with open('P_{}'.format(file_name), 'w') as f:
    for t in range(num_of_sec):
        for freq in range(num_of_freq - 1):
            f.write(new_lines[t][freq] + ',')
        else:
            f.write(new_lines[t][-1])
            f.write('\n')
