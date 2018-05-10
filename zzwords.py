#Christo Dragnev
#5/10/18
#zzwords.py

file = open('engmix.txt')

for word in file:
    if 'zz' in word:
        print(word.strip())
