'''
Задача 1
'''

# spisok = [[3, 7, 8, 9], [2, 4, 5]]
# maxE = spisok[0][0]
# maxI = 0
# maxJ = 0

# for i in range(len(spisok)):
#     for j in range(len(spisok[i])):
#         if spisok[i][j] > maxE:
#             maxE = spisok[i][j]
#             maxI = i
#             maxJ = j
# print(f"{maxE} в {maxI + 1} строке элемент {maxJ +1}")

'''
Задача 2
'''
# n = int(input("Нечетное число: "))
# sneg = [['.'] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == (n // 2) or j == (n // 2) or i == j or (i + j) == n - 1:
#             sneg[i][j] = '*'
#     print(' '.join(sneg[i]))

'''
Задача 3
'''

n, m = [int(i) for i in input().split()]
a = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            a[i][j] = '*'
    print(' '.join(a[i]))
