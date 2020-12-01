#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = input('Введите слово')

def recerse_string(n):
    return "".join(reversed(n))

s = recerse_string(n)

if s == n:
    print(f'Слово {n} является палиндромом')
else:
    print(f"Слово {n} не является палиндромом")

