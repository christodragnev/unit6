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
'''
new = []
for line in file:
    line = line.strip()
    if len(line) > 0:
        new.append(line)
        if line[0] == line[4] and line[8] == line[4]:
            print(line)
'''
        
#3
'''
num = int(input('Enter a number: '))
letter = input('Enter a letter: ')
new = []
for line in file:
    line = line.strip()
    if len(line) > 0:
        new.append(line)
        if letter == line[0] and num == len(line):
            print(line)
'''

#4
new = []
for line in file:
    line = line.strip()
    if len(line) >= 10:
        new.append(line)
    print(new[7999])
    