def bubble_sort(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                is_sorted = False

    return array


def main():
    length = int(input())
    print(" ".join(bubble_sort(input().split())))
    

if __name__ == "__main__":
    main()