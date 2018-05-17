#Christo Dragnev
#5/17/18
#longShort.py

file = open('engmix.txt')


alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = []
for line in file:
    line = line.strip()
    L.append(line)
