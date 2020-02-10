if __name__ == '__main__':
    i = int(input())
    lst = list(map(int, input().strip().split()))[:i]
    z = max(lst)

    while max(lst) == z:
        lst.remove(max(lst))

    print(max(lst))
