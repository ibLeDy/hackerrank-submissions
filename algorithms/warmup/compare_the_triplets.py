import os


def compareTriplets(a, b):
    result = []
    ra = 0
    rb = 0

    if a[0] > b[0]:
        ra += 1
    if a[1] > b[1]:
        ra += 1
    if a[2] > b[2]:
        ra += 1

    if a[0] < b[0]:
        rb += 1
    if a[1] < b[1]:
        rb += 1
    if a[2] < b[2]:
        rb += 1

    if a[0] == b[0]:
        pass
    if a[1] == b[1]:
        pass
    if a[2] == b[2]:
        pass

    result = [ra, rb]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
