#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input().split()))

    # Нахождение нулевых элементов и минимального элемента
    n = 0
    a_min = a[0]
    i_min = 0
    for ind, value in enumerate(a):
        if value == 0:
            n += 1
        if value < a_min:
            a_min = value
            i_min = ind
    print(f"Количество нулевых элементов: {n}")

    # Нахождение суммы элементов после минимального
    a1 = a[i_min + 1:]
    s = sum(i for i in a1)
    print(f"Сумма элементов после минимального : {s}")

    # Сортировка
    i = 0
    while i < len(a):
        j = 0
        while j < len(a) - 1:
            if abs(a[j]) > abs(a[j + 1]):
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1
    print(f"Отсортированный список: {a}")
