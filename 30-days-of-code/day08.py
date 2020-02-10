n = int(input())
result = {}


while n > 0:
    n -= 1

    data = list(map(str, input().strip().split(" ")))
    result[data[0]] = data[1]

while True:
    query = str(input())

    if query in result.keys():
        print("{}={}".format(query, result[query]))
    else:
        print("Not found")
