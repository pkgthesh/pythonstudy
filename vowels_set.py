vowels = set ('aeiou')
word = input("Provide a word to search for vowels: ")
letter = vowels.intersection(set(word))
print (letter)
