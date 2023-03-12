def is_palindrome(word):
    return word == word[::-1]


while True:
    word = input("Ingrese una palabra: ")
    if is_palindrome(word):
        print("---> La palabra es palindroma")
    else:
        print("---> La palabra no es palindroma")
