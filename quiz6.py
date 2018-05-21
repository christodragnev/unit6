#Christo Dragnev
#5/21/18
#quiz6.py

file = open('engmix.txt')

#Program1
'''
letter = input('Enter a letter: ')
for line in file:
    line = line.strip()
    if line.count(letter)==4:
        print(line)
'''

#Program2
'''
new = []
for line in file:
    line = line.strip()
    if len(line)>9:
        new.append(line)

for word in new:
    if word[0] == word[4] and word[4] == word[8]:
        print(word)
        break
'''
        
#Program3
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

#Program4
'''
new = []
for line in file:
    line = line.strip()
    if len(line)>=10:
        new.append(line)
print(new[7999])
'''

    
    