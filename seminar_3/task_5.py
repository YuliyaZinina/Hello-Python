# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def negafib(m):
    if m == 0:
        return 0
    elif m == -1:
        return 1
    elif m == -2:
        return -1
    else:
        return negafib(m + 2) - negafib(m + 1)


number = 8
list_fib = []
for e in range(-number, 1):
    list_fib.append(negafib(e))
for e in range(1, number+1):
    list_fib.append(fib(e))

print(list_fib)
