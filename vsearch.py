def search4vowels(word):
        """ Display any vowels found in a supplied word."""
        vowels = set ('aeiou')
        found = vowels.intersection(set(word))
        for vowels in found:
                print(vowels)
