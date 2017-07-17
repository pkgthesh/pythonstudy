def search4vowels(word):
        """ Return a boolean based on any vowels found"""
        vowels = set ('aeiou')
        return vowels.intersection(set(word))
