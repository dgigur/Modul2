number = int(input('Введите число от 3 до 20: '))
password = []


def uniq(list_1, a, b):
    in_list = False
    if len(list_1) == 0:  # Если список пустой то вернем что чисел нет в списке
        return in_list
    for k in range(0, len(list_1), 2):  # Прогоним проверку наличия пары чисел в списке
        if [a, b] == reversed([list_1[k], list_1[k + 1]]):  # Идентичной пары быть не может поэтому только обратная
            in_list = True
            break
    return in_list


for i in range(1, number):
    for j in range(i + 1, number):
        if j == i:
            continue
        elif number % (i + j) == 0:
            if not uniq(password, i, j):  # Если флаг остался 0 то добавим пару чисел
                password.extend([i, j])

print(*password)
for i in range(len(password)):
    password[i] = str(password[i])
print(''.join(password))
