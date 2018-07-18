def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    swv = ""
    for letter in s:
        if not (letter in vowels):
            swv += letter
    print(swv)