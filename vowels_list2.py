vovels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = []
for i in word:
    if i in vovels:
            if i not in found:
                found.append(i)
for letter in found:
    print (letter)
