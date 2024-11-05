#!/usr/bin/env python3
import sys
import math

try:
    result = float(input().strip())
    if result < 0:
        raise ValueError("Необходимо ввести неотрицательное число")
    sqrt_result = math.sqrt(result)
    with open("output.txt", "w") as f:
        f.write(str(sqrt_result))
except Exception as e:
    print(f"Ошибка в программе squareRoot: {e}", file=sys.stderr)
