from random_array import get_random_array
from sort import selection_sort, bubble_sort, quick_sort


def average(array):
    sum = 0
    for i in array:
        sum += i
    return i/len(array)


def get_ten_first(array):
    new_array = []
    for x in range(10):
        new_array.append(array[x])
    return new_array


def get_ten_last(array):
    new_array = []
    length = len(new_array)
    for x in range(10, 0, -1):
        new_array.append(array[length-1-x])
    return new_array


if __name__ == "__main__":
    print("--- Generando Array ---")
    array = get_random_array()

    print("Array generado, su tamaño es:", len(array))
    print("--- Ordenamiento utilizando Selection Sort ---")
    print("Creando una copia del array")
    copy = array.copy()
    print("Copia del array creada")
    print("Ordenando el array")
    selection_sort(copy)
    print("Array ordenado")
    print("Los primeros diez son:", get_ten_first(copy))
    print("Los ultimos diez son:", get_ten_last(copy))

    print("--- Ordenamiento utilizando Bubble Sort ---")
    print("Creando una copia del array")
    copy = array.copy()
    print("Copia del array creada")
    print("Ordenando el array")
    bubble_sort(copy)
    print("Array ordenado")
    print("Los primeros diez son:", get_ten_first(copy))
    print("Los ultimos diez son:", get_ten_last(copy))

    print("--- Ordenamiento utilizando Quick Sort ---")
    print("Creando una copia del array")
    copy = array.copy()
    print("Copia del array creada")
    print("Ordenando el array")
    quick_sort(copy)
    print("Array ordenado")
    print("Los primeros diez son:", get_ten_first(copy))
    print("Los ultimos diez son:", get_ten_last(copy))

    print("--- Calculando el maximo, minimo y promedio ---")
    print("El maximo es:", copy[len(copy)-1])
    print("El minimo es:", copy[0])
    print("El promedio es:", average(copy))
