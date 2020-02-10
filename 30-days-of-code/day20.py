n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def bubbleSort(arr):
    number_of_swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                number_of_swaps += 1

    return arr, number_of_swaps


arr, n = bubbleSort(a)
number_of_swaps = n

print("Array is sorted in {} swaps.".format(number_of_swaps))
print("First Element: {}".format(arr[0]))
print("Last Element: {}".format(arr[-1]))
