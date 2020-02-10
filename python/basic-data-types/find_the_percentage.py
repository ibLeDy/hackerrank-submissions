if __name__ == '__main__':
    n = int(input())

    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    result = 00.00

    for i in student_marks[query_name]:
        result += i

    requested = result / len(student_marks[query_name])
    result = 00.00

    print("{:.2f}".format(requested))
