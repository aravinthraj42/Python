text = input('Enter Some text: ')
word = text.split()
print(word)
count = 0
for w in word:
    count += 1
print('Number of words in the entered text is:', count)
#word.sort()

print('The words in sorted order are: ')
for w in word:
    print(w)
