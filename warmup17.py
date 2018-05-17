#Christo Dragnev
#5/17/18
#warmup17.py - find all words that contain every letter of your last name

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if 'd' in line and 'r' in line and 'a' in line and 'g' in line and 'n' in line and 'e' in line and 'v' in line:
        print(line)
