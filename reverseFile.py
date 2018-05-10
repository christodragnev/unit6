#Christo Dragnev
#5/10/18
#reverseFile.py

file = open(input('Enter file name: '))


new = []
for line in file:
    if len(line)>0:
        new.append(line.strip(\n))
print(new)
    
    
    
