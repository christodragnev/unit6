#Christo Dragnev
#5/21/18
#quiz6.py

file = open('engmix.txt')

#1
"""
letter = input('Enter a letter: ')
for line in file:
    line = line.strip()
    if line.count(letter)==4:
        print(line)
"""

#2
new = []
for line in file:
    line = line.strip()
    if len(line) > 0: