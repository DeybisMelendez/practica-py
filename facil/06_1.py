num = int(input("Ingrese un numero: "))


def fizzbuzz(num):
    result = ""
    if num % 3 == 0:
        result += "fizz"
    if num % 5 == 0:
        result += "buzz"
    if not result:
        result = str(num)
    return result


print("El numero ingresado es:", fizzbuzz(num))
