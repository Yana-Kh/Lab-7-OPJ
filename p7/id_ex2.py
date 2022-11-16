#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


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

    # Нахождение суммы элементов после минимального
    a1 = a[i_min + 1:]
    summ = sum(i for i in a1)
    print(f"Сумма элементов после минимального : {summ}")

    # Сортировка
    def abs_func(x1, x2):
        if abs(float(x1)) > abs(float(x2)):
            return 1
        else:
            return -1
    a.sort(key=functools.cmp_to_key(abs_func))
    print(f"Отсортированный список: {a}")
