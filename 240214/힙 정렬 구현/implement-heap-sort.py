def heapify(array, n, i):
    largest_index = i
    left_index = i*2
    right_index = i*2+1

    if left_index <= n and array[left_index] > array[largest_index]:
        largest_index = left_index
    
    if right_index <= n and array[right_index] > array[largest_index]:
        largest_index = right_index

    if largest_index != i:
        array[i], array[largest_index] = array[largest_index], array[i]
        heapify(array, n, largest_index)

def heap_sort(array, n):
    for i in range(n//2, 0, -1):
        heapify(array, n, i)

    for i in range(n, 1, -1):
        array[1], array[i] = array[i], array[1]
        heapify(array, i-1, 1)


length = int(input())
array = [0] + list(map(int, input().split()))
heap_sort(array, length)

for element in array[1:]:
    print(element, end=" ")