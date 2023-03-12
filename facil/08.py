def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


word1 = input("Ingrese una palabra: ")
word2 = input("Ingrese otra palabra: ")

if is_anagram(word1, word2):
    print(word2, "es anagrama de", word1)
else:
    print(word2, "no es anagrama de", word1)
