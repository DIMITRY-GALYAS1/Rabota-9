#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = str(input('Введите первую строку:'))
    s2 = str(input('Введите вторую строку:'))
    u = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМ'
            'НОПРТСУФХЦЧШЩЪЫЬЭЮЯ')
    d = set(s1)
    q = set(s2)
    d.remove(' ')
    q.remove(' ')
    x = (d.intersection(q))
    print(f"x = {x}")
