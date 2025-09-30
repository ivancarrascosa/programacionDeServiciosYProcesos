"""Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal."""
def vowel(char):
    isVowel = False
    vowels = ["a","e","i","o","u"]
    if char in vowels:
        isVowel = True
    return isVowel

print(vowel("f"))