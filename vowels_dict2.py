vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
for i in word:
    if i in vowels:
        found.setdefault(i, 0)
        found[i] += 1
for k, v in sorted(found.items()):
    print (k, 'was found', v, 'time(s).')
