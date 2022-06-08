import random

RUN = 64

def insertionSort(arr, left, rigth):
    for i in range(left + 1, rigth+1):

        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, rigth = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        rigth.append(arr[m + 1 + i])

    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= rigth[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = rigth[j]
            j += 1
        k += 1

    while i < len1:

        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = rigth[j]
        k += 1
        j += 1

def timSort(arr, n):
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i+31), (n-1)))

    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            rigth = min((left + 2*size - 1), (n-1))
            merge(arr, left, mid, rigth)
        size = 2*size

def printArray(arr, n):

    for i in range(0, n):
        print(arr[i], end =" ")
    print()

if __name__=="__main__":

    arr = [5, 21, 7, 23, 19] 
    n = len(arr) 

    timSort(arr, n) 

    printArray(arr, n) 