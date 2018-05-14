file = open('engmix.txt')
word = input('Enter a word: ')

end = 0
while end == 0:
    for line in file:
        if word == line.strip():
            print(word, 'is in the dictionary')
            end+=1
        elif word != line.strip():
            print(word, 'is not in the dictionary')
            end+=1
        
        
            