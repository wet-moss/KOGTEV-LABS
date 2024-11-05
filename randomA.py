#!/usr/bin/env python3
import random
import sys

try:
    A = random.randint(-10, 10)
    print(A)
except Exception as e:
    print(f"Ошибка в программе randomA: {e}", file=sys.stderr)