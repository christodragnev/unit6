#Christo Dragnev
#5/10/18
#howManyWords.py

file = open('engmix.txt')

L = [0]*22
for word in file:
    L[len(word)-1] = L[len(word)-1] + 1
    
i = 1
while i<=21:
    print(i,'- letter words:',L[i])
    i+=1