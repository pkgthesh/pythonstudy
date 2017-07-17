def search4vowels(word:str) -> set:
        """ Return a boolean based on any vowels found"""
        vowels = set ('aeiou')
        return vowels.intersection(set(word))
