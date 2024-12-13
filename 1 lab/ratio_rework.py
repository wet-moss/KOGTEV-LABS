#!/usr/bin/env python3
import random
import sys

def main():
    try:
        line = sys.stdin.readline().strip()
        if not line:
            raise ValueError("Нет данных для A")
        A = int(line)
        B = random.randint(-10, 10)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"A={A}, B={B}\n")
        result = A / B
        print(result)

    except ValueError as ve:
        print(f"Ошибка ввода: {ve}", file=sys.stderr)
    except ZeroDivisionError as zve:
        print(f"Ошибка (деление на ноль): {zve}", file=sys.stderr)
    except Exception as e:
        print(f"Произошла ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
