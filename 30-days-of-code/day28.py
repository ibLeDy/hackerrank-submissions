import re

pattern = re.compile(r'^[a-z\.]+@gmail.com$')
N = int(input())

valid_names = []
for row in range(N):
    first_name, email_id = input().split()

    if pattern.match(email_id):
        valid_names.append(first_name)

for name in sorted(valid_names):
    print(name)
