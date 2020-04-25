import os


def simpleArraySum(ar):
    return sum(a for a in ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()
