def merge_sort(array, low_index, high_index):
    if low_index < high_index:
        mid_index = (low_index + high_index) // 2
        merge_sort(array, low_index, mid_index)
        merge_sort(array, mid_index+1, high_index)
        merge(array, low_index, mid_index, high_index)

    return array

def merge(array, low_index, mid_index, high_index):
    i = low_index
    j = mid_index + 1

    array_merged = []
    while i <= mid_index and j <= high_index:
        if array[i] <= array[j]:
            array_merged.append(array[i])
            i += 1
        else:
            array_merged.append(array[j])
            j += 1

    while i <= mid_index:
        array_merged.append(array[i])
        i += 1

    while j <= high_index:
        array_merged.append(array[j])
        j += 1

    array[low_index:high_index+1] = array_merged

length = int(input())
array = list(map(int, input().split()))
for element in merge_sort(array, 0, length-1):
    print(element, end=" ")