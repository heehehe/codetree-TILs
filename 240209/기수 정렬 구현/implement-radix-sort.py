MAX_K = 6
MAX_DIGIT = 10

length = int(input())

def radix_sort(array):
    p = 1
    for position in range(MAX_K):
        array_new = [[] for _ in range(MAX_DIGIT)]
        for element in array:
            digit = (element // p) % 10
            array_new[digit].append(element)
        
        array = []
        for digit in range(MAX_DIGIT):
            for element in array_new[digit]:
                array.append(element)

    p *= 10

    return array


for element in radix_sort(list(map(int, input().split()))):
    print(element, end=" ")