import os


def reverseArray(a):
    result = a[::-1]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
