#Christo Dragnev
#5/10/18
#longestDictionaryWord.py

file = open('engmix.txt')

longest = ''
for word in file:
    if len(word)>len(longest):
        longest = word
print(longest)