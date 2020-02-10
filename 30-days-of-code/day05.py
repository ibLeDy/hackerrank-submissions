n = int(input())
times = 0
multiplier = 0
result = 0

while times < 10:
    multiplier += 1
    result = int(n * multiplier)
    times += 1

    print(f"{n} x {multiplier} = {result}")
