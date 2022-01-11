#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    arr = list(map(float, input("Введите спискок:\n").split()))
    position = arr.index(min(arr))
    first_neg = -1
    second_neg = -1
    arr1 = []
    arr2 = []
    for pos, elem in enumerate(arr):
        if elem < 0:
            if first_neg == -1:
                first_neg = pos
            elif second_neg == -1:
                second_neg = pos
        if -1 <= elem <= 1:
            arr1.append(elem)
        else:
            arr2.append(elem)
    summa = sum(arr[first_neg + 1:second_neg])
    result = arr1 + arr2
    print(f"Позиция минимального элемента = {position}")
    print(f"Сумма между первым и втормы отрицательным элемнтом = {summa}")
    print(f"Приобразованный список = {result}")
