from datetime import date

d1, m1, y1 = list(map(int, input().split()))
d2, m2, y2 = list(map(int, input().split()))

actual = date(y1, m1, d1)
expected = date(y2, m2, d2)
fine = 0

if actual > expected:
    if actual.year == expected.year:
        if actual.month == expected.month:
            fine = 15 * (actual.day - expected.day)
        else:
            fine = 500 * (actual.month - expected.month)
    else:
        fine = 10000

print(fine)
