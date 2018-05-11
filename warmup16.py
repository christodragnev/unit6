#Christo Dragnev
#5/12/18
#warmup16.py - prints out all words that start with your initial and end with your last inital

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if len(line) > 0:
        if 'c' in line[0] and 'o' in line[-1]:
            print(line)
        