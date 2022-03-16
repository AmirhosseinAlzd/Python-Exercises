Sentence = input('Plz Write your Sentence to count its words :\n\n\t==> ').strip()
Counter_space = 0
for char in Sentence :
    if char == ' ':
        Counter_space +=1

print('Number of Words : ' , Counter_space+1)