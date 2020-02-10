n = int(input())
s = set(map(int, input().split()))

N = int(input())
for i in range(N):
    element = input()

    if element.startswith("pop"):
        s.pop()
    elif element.startswith("remove"):
        command, value = element.split()
        s.remove(int(value))
    elif element.startswith("discard"):
        command, value = element.split()
        s.discard(int(value))

print(sum(s))
