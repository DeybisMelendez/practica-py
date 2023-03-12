def selection_sort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])


def bubble_sort(array):
    size = len(array)
    swapped = False
    for i in range(size-1):
        for j in range(0, size-i-1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _partition(array, begin, end):
        pivot = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot

    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = _partition(array, begin, end)
        _quick_sort(array, begin, pivot-1)
        _quick_sort(array, pivot+1, end)
    return _quick_sort(array, begin, end)
