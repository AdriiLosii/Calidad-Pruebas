#!/usr/bin/env python3
# encoding: utf-8

import random

def ordenamiento_por_insercion(data):
    for i in range(1, len(data)):
        elemento = data[i]
        j = i - 1
        print(j>=0)
        print(data[j] > elemento)
        while (j >= 0 and data[j] > elemento):
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = elemento
    return data

if __name__ == '__main__':
    data = [random.randint(0, 9) for _ in range(2)]
    print(data, "->", ordenamiento_por_insercion(data.copy()))