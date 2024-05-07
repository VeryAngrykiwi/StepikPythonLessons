#ЗАПОЛНЕНИЕ 1

# Вариант 1
n, m = map(int, input().split())

mtx = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    mtx[i][j] = i * n + j + 1
    print(str(mtx[i][j]).ljust(3), end='')
  print()

# Вариант 2

n, m = map(int, input().split())

# Создаем матрицу с индексами от 1 до n*m
matrix = [[(i * m + j + 1) for j in range(m)] for i in range(n)]

# Выводим матрицу
for row in matrix:
    print(' '.join(str(x).ljust(3) for x in row))


# Вариант 3
x = input().split() #Вводная строка
n, m = int(x[0]), int(x[1]) #присвоение значений с вводной строки

mtx = [] #матрица - пустой список 
for _ in range(n): #цикл наполнения матрицы
  tmp = [el for el in range(m)] # ввод переменной для заполнения матрицы (пустое значение)
  mtx.append(tmp) # дополнение матрицы.

count = 1 #счетчик 
for i in range(n): # цикл заполнения матрицы числами + 1
  for q in range(m):
    mtx[i][q] = count
    count += 1 # увеличение счетчика на 1

for i in range(n): # цикл вывода матрицы
  for q in range(m):
    print(str(mtx[i][q]).ljust(3), end='') #перевод в строку, дополнение пробелов
  print() # построчный вывод



'''
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()



n, m = [int(i) for i in input().split()]
matrix = [list(range(m*i + 1, m*i + 1 + m)) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()



n, m = [int(i) for i in input().split()]

for i in range(1, (n * m) + 1):
    print(str(i).ljust(2), end=' ')
    if i % m == 0:
        print()



[n, m] = [int(i) for i in input().split()]
mtx = [ [0] * m for _ in range(n)]
ind = 1
for i in range(n):
    for j in range(m):
        mtx[i][j] = ind
        ind += 1
for i in range(n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(3), end=' ')
    print()



n, m = map(int, input().split())
for i in range(n):
    row = [str(i * m + j).ljust(3, ' ') for j in range(1, m + 1)]
    print(*row)



n, m = map(int, input().split())

count = 1

for i in range(n):
    for j in range(m):
        print(f'{count:3}', end=' ')
        count += 1
    print()



n, m = map(int, input().split())
[print(*(str(i * m + j).ljust(3) for j in range(1, m + 1))) for i in range(n)]



# принимаем n и m, разделяем и плучаем i and j
nm = input().split()
n, m = int(nm[0]), int(nm[1])
matrix, num = [], 1
# создаем матрицу и заполняем
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(j)
    matrix.append(temp)
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1
# вывод нарядной матрицы
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()



# принимаем n и m, разделяем и плучаем i and j
nm = input().split()
n, m = int(nm[0]), int(nm[1])
matrix, num = [], 1
# создаем матрицу и заполняем
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(j)
    matrix.append(temp)
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1
# вывод нарядной матрицы
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()



n, m = [int(x) for x in input().split()]

a = [[0] * m for _ in range(n)]
x = 1
for i in range(n):
    for j in range(m):
        a[i][j] = str(x).ljust(2)
        x += 1


[print(*s) for s in a]
'''


# ЗАПРОЛНЕНИЕ 2

x = input().split() #Вводная строка
n, m = int(x[0]), int(x[1]) #присвоение значений с вводной строки

mtx = [] #матрица - пустой список 
for _ in range(n): #цикл наполнения матрицы
  tmp = [el for el in range(m)] # ввод переменной для заполнения матрицы (пустое значение)
  mtx.append(tmp) # дополнение матрицы.

count = 1 #счетчик 
for q in range(m): # цикл заполнения матрицы числами + 1
  for i in range(n):
#    mtx[i][q] = i+q*n+1 #заполнение матрицы постолбцам
    mtx[i][q] = count
    count += 1 # увеличение счетчика на 1

for i in range(n): # цикл вывода матрицы
  for q in range(m):
    print(str(mtx[i][q]).ljust(3), end='') #перевод в строку, дополнение пробелов
  print() # построчный вывод

'''
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()



n, m = [int(i) for i in input().split()]
matrix = [
    list(range(i + 1, i + 1 + n * (m - 1) + 1, n))
    for i in range(n)
]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()







'''



