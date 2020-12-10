#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано слово. Проверить, является ли оно палиндромом
if __name__ == '__main__':
    n = input('Введите слово')

    def recerse_string(n):
        return "".join(reversed(n))

    s = recerse_string(n)

    if s == n:
        print(f'Слово {n} является палиндромом')
    else:
        print(f"Слово {n} не является палиндромом")

