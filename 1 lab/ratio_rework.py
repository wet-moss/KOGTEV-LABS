#!/usr/bin/env python3
import random
import sys

def main():
    try:
        line = sys.stdin.readline().strip()
        A = int(line)
        B = random.randint(-10, 10)
        result = A / B
        print(result)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"A = {A}, B = {B}, A / B = {result}\n")
    except ZeroDivisionError as zve:
        with open("logs.txt", "a") as log_file:
            log_file.write(f"A = {A}, B = {B}\n")
        with open("errors.txt", "a") as error_file:
            error_file.write(f"Ошибка (деление на ноль): {zve}\n")
        print(f"Ошибка (деление на ноль): {zve}", file=sys.stderr)
    except Exception as e:
        with open("errors.txt", "a") as error_file:
            error_file.write(f"Ошибка: {e}\n")
        print(f"Произошла ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
