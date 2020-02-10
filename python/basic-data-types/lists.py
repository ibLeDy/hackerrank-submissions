if __name__ == '__main__':
    N = int(input())
    commands = []
    result = []

    i = 0
    while i < N:
        a = input()
        commands.append(a)
        i += 1

    for foo in commands:
        if "insert" in foo:
            ins = foo.split()
            i = int(ins[1])
            o = int(ins[2])
            result.insert(i, o)
        elif "print" in foo:
            print(result)
        elif "remove" in foo:
            ins = foo.split()
            ins = ins[1]
            result.remove(int(ins))
        elif "append" in foo:
            ins = foo.split()
            ins = ins[1]
            result.append(int(ins))
        elif "sort" in foo:
            result.sort()
        elif "pop" in foo:
            result.pop()
        elif "reverse" in foo:
            result.reverse()
        else:
            pass
