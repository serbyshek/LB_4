#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    st = input('Введите предложение')
    mx = [0]
    c = 0
    for i in range(len(st)):
     if st[i] == ' ':
        mx[c] += 1
     elif st[i] != ' ' and st[i-1] == ' ':
        c += 1
        mx.append(0)
    print(max(mx))
