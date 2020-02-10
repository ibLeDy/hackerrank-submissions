import collections


N = int(input())
result = collections.deque()

for i in range(N):
    element = input().split()

    if len(element) > 1:
        name, value = element
    else:
        name = element[0]

    if name == "append":
        result.append(value)
    elif name == "appendleft":
        result.appendleft(value)
    elif name == "pop":
        result.pop()
    elif name == "popleft":
        result.popleft()

print(*result)
