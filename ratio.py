#!/usr/bin/env python3
import random
import sys

try:
    A = int(input().strip())
    B = random.randint(-10, 10)
    if B == 0:
        raise ValueError("Попытка деления на ноль")
    result = A / B
    print(result)
except Exception as e:
    print(f"Ошибка в программе ratio: {e}", file=sys.stderr)
