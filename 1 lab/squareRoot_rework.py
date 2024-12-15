#!/usr/bin/env python3
import sys
import math

def main():
    try:
        line = sys.stdin.readline().strip()
        num = float(line)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"C = {num}\n")
        sqrt_result = math.sqrt(num)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"C^0.5 = {sqrt_result}\n\n")
        with open("output.txt", "a") as output_file:
            output_file.write(f"{sqrt_result}\n")
    except ValueError:
        with open("logs.txt", "a") as log_file:
            log_file.write(f"C = {num}\n\n")
        with open("errors.txt", "a") as error_file:
            error_file.write(f"Невозможно вычислить квадратный корень при C = {num}\n")
        print(f"Ошибка ввода: Невозможно вычислить корень из {num}", file=sys.stderr)
    except Exception as e:
        with open("errors.txt", "a") as error_file:
            error_file.write(f"Ошибка: {e}\n")
        print(f"Произошла ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
