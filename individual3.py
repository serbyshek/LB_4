#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input('Введите слово'))
    k = int(input('Введите порядковый номер буквы, которую желаете удалить'))
    с = k + 1


    v = s[:k] + s[с:]
    j = s[:3] + s[4:]

    print(f'В слове {s} удалена третья буква {j}. В слове {s} удалена {k}-я буква {v}')