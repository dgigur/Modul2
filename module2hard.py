number = int(input('Введите число от 3 до 20: '))
password = []


def uniq(list_1, a, b):
    in_list = False
    if len(list_1) == 0:
        password.append([a, b])
        return
    else:
        for k in range(0, len(list_1)):
            if [a, b] == reversed(list_1[k]):
                in_list = True
                break
    if not in_list:
        password.append([a, b])


for i in range(1, number):
    for j in range(i + 1, number):
        if j == i:
            continue
        elif number % (i + j) == 0:
            uniq(password, i, j)

print(password)


#Это чтобы вывести ответ как в задании
'''
password1 = []
for i in range(len(password)):
    password1.extend(password[i])
for i in range(len(password1)):
    password1[i] = str(password1[i])
print(''.join(password1))
'''
