n = int(input())
arr = list(map(int, input().rstrip().split()))

print(' '.join(str(i) for i in arr[::-1]))
