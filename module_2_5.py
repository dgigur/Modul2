def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


#print(get_matrix(2, 2, 10))
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

"""
def get_matrix1(*args):
    matrix = []
    for i in range(args[0]):
        matrix.append([])
        for j in range(args[1]):
            matrix[i].append(args[2])
    return matrix


print(get_matrix1(2, 2, 10))
"""
'''
dictionary = {}
def dict(**kwargs):
    dictionary.update(kwargs)
    print(dictionary)
    return dictionary


print(dictionary)
dict(jek123a='pu123l')
dict(kolya = 'askjko')
dict(vasya = '22', polya = 8)
'''