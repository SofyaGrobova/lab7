#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    arr = list(map(int, input("Введите спискок:\n").split(' ')))
    if len(arr) != 10:
        print("Неверный размер списка", file=sys.stderr)
    else:
        multiplication = 1
        for elem in arr:
            if elem < 0:
                multiplication *= elem
        print(f"Произведение отрицательных чисел = {multiplication}")
