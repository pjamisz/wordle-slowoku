def utf8len(s):
    return len(s.encode('utf-8'))


words = list(open('slowa.txt', encoding = 'utf8').read().split())

print(words[0:10])
print(len(words[0]))

with open('words_five_letters.txt', 'w', encoding= 'utf8') as my_file:
    for word in words:
        if len(word) == 5:
            my_file.write(word + '\n')

print(len(words))