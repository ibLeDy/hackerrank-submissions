import os


def aVeryBigSum(ar):
    result = sum(a for a in ar)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()
