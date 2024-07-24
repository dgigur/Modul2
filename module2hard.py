number = int(input('Введите число от 3 до 20: '))
password = []


def uniq(list_1, a, b):
    in_list = False
    if len(list_1) == 0:
        password.extend([a, b])
        return
    else:
        for k in range(0, len(list_1), 2):
            if [a, b] == reversed([list_1[k], list_1[k+1]]):
                in_list = True
                break
    if not in_list:
        password.extend([a, b])


for i in range(1, number):
    for j in range(i + 1, number):
        if j == i:
            continue
        elif number % (i + j) == 0:
            uniq(password, i, j)

print(*password)
for i in range(len(password)):
    password[i] = str(password[i])
print(''.join(password))
