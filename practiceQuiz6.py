#Christo Dragnev
#5/18/18
#practiceQuiz6.py

#Program1
file = open('engmix.txt')

for line in file:
    line = line.strip()
    if line.count('c')==3 and line.count('p')==2:
        print(line)
        
#program3
num = int(input('Enter a number: ')

