if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        max_ab = 0

        for a in range(n - 1, 1, -1):
            for b in range(n, a, -1):
                ab = a & b

                if ab < k and ab > max_ab:
                    max_ab = ab

                if max_ab == k - 1:
                    break

            if max_ab == k - 1:
                break

        print(max_ab)
