def selection_sort(array):
    for i in range(len(array)):
        min_element = i
        for j in range(i, len(array)):
            if array[j] < array[min_element]:
                min_element = j
        array[min_element], array[i] = array[i], array[min_element]

    return array

length = int(input())
for element in selection_sort(list(map(int, input().split()))):
    print(element, end=" ")