#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s = str(input('Введите строку:'))
    gl = set("ёуеыаоэяиюЁУЕЫАОЭЯИЮ")
    count = 0
    for z in s:
        if z in gl:
            count += 1
    print('Количество гласных букв', count)
