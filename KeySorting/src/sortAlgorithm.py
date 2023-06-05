def bubbleSort(array, order):
    trade = True
    while (trade is True):
        trade = False
        for i in range(0, len(array) - 1):
            if array[i].chave > array[i+1].chave and order == 'C':
                array[i], array[i+1] = array[i+1], array[i]
                trade = True
            if array[i].chave < array[i+1].chave and order == 'D':
                array[i], array[i+1] = array[i+1], array[i]
                trade = True
    return array

def selectionSort(array, order):
    for i in range(0, len(array) - 1):
        lower = i
        for j in range(i + 1, len(array)):
            if array[j].chave < array[lower].chave and order == 'C':
                lower = j
            if array[lower].chave > array[j].chave and order == 'D':
                lower = j
        array[i], array[lower] = array[lower], array[i]
    return array

def insertionSort(array, order):
    for i in range(1, len(array)):
        tmp = array[i]
        index = i - 1
        if order == 'C':
            while(index >= 0 and tmp.chave < array[index].chave):
                array[index + 1] = array[index]
                index = index - 1
        elif order == 'D':
            while(index >= 0 and tmp.chave > array[index].chave):
                array[index + 1] = array[index]
                index = index - 1
        array[index + 1] = tmp
    return array

def merge(array, first, last, order):
    i = j = k = 0
    if order == 'C':
        while i < len(first) and j < len(last):
            if first[i].chave < last[j].chave:
                array[k] = first[i]
                i += 1
            else:
                array[k] = last[j]
                j += 1
            k += 1
    elif order == 'D':
        while i < len(first) and j < len(last):
            if first[i].chave > last[j].chave:
                array[k] = first[i]
                i += 1
            else:
                array[k] = last[j]
                j += 1
            k += 1
    while i < len(first):
        array[k] = first[i]
        i += 1
        k += 1
    while j < len(last):
        array[k] = last[j]
        j += 1
        k += 1
    return array

def __mergeSort(array, order):
    if len(array) > 1:
        middle = len(array) // 2
        first = array[:middle]
        last = array[middle:]
        mergeSort(first, order)
        mergeSort(last, order)
        merge(array, first, last, order)

def mergeSort(array, order):
    __mergeSort(array, order)
    return array

def partition(array, start, end, order):
    pivot = array[start].chave
    left = start + 1
    right = end
    if order == 'C':
        while (True):
            while (left <= right and array[left].chave <= pivot):
                left = left + 1
            while (array[right].chave >= pivot and right >= left):
                right = right - 1
            if left < right:
                array[left], array[right] = array[right], array[left]
            else:
                break
        array[start], array[right] = array[right], array[start]
    if order == 'D':
        while (True):
            while (left <= right and array[left].chave >= pivot):
                left = left + 1
            while (array[right].chave <= pivot and right >= left):
                right = right - 1
            if left < right:
                array[left], array[right] = array[right], array[left]
            else:
                break
        array[start], array[right] = array[right], array[start]
    return right

def __quickSort(array, start, end, order):
    if (start < end):
        split = partition(array, start, end, order) # pivo
        __quickSort(array, split + 1, end, order)
        __quickSort(array, start, split - 1, order)

def quickSort(array, order):
    __quickSort(array, 0, len(array) - 1, order)
    return array

def maxHeapify(array, index, heapSize, order):
    left  = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if order == 'C':
        if(left <= (heapSize - 1)) and (array[left].chave > array[index].chave):
            largest = left
        if (right <= (heapSize - 1)) and (array[right].chave > array[largest].chave):
            largest = right
        if index != largest:
            array[index], array[largest] = array[largest], array[index]
            maxHeapify(array, largest, heapSize - 1, order)
    if order == 'D':
        if(left <= (heapSize - 1)) and (array[left].chave < array[index].chave):
            largest = left
        if (right <= (heapSize - 1)) and (array[right].chave < array[largest].chave):
            largest = right
    if index != largest:
        array[index], array[largest] = array[largest], array[index]
        maxHeapify(array, largest, heapSize - 1, order)


def buildMaxHeap(array, heapSize, order):
    indexes = range(len(array) // 2, -1, -1)
    for index in indexes:
        maxHeapify(array, index, heapSize, order)

def heapSort(array, order):
    heapSize = len(array)
    buildMaxHeap(array, heapSize, order)
    indexes = range(len(array)-1, 0, -1)
    for index in indexes:
        array[0], array[index] = array[index], array[0]
        heapSize = heapSize - 1
        maxHeapify(array, 0, heapSize, order)
    return array
