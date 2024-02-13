def partition(array, low, high):
    pivot = array[high]
    i = low-1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low, high):
    if low < high:
        index = partition(array, low, high)
        quick_sort(array, low, index-1)
        quick_sort(array, index+1, high)

    return array

length = int(input())
array = list(map(int, input().split()))
quick_sort(array, 0, length-1)

for element in array:
    print(element, end=" ")