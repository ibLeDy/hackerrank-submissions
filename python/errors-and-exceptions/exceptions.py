T = int(input())

for i in range(T):
    try:
        a, b = map(int, input().split(" "))
        print(a // b)
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)
