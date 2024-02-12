
def bubble_sort(arr):
    size = len(arr)
    
    for i in range(size -1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def insertion_sort(arr):
    size = len(arr)

    for i in range(1, size):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp

            j -= 1

def merge_two_list(a, b):
    c = []
    i = j = 0

    while i < len(a) and j < len(b) :
        if a[i] < b[j] :
            c.append(a[i])
            i+= 1
        else :
            c.append(b[j])
            j+= 1
    
    c += a[i:] + b[j:]

    return c

def merge_sort(arr):
    size = len(arr)
    middle = size // 2

    if size <= 1:
        return arr
    
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge_two_list(left, right)



arr = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
bubble_sort(arr)
print("Bubble sort:", arr)

arr = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
insertion_sort(arr)
print("Insertion sort:", arr)

arr = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
print("Merge sort:", merge_sort(arr))


