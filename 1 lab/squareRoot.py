#!/usr/bin/env python3
import sys
import math

def main():
    try:
        num = float(input("Введите неотрицательное число: ").strip())
        if num < 0:
            raise ValueError("Необходимо ввести неотрицательное число")   
        sqrt_result = math.sqrt(num) 
        with open("output.txt", "a") as f:
            f.write(f"{sqrt_result}\n")
        
    except ValueError as ve:
        print(f"Ошибка ввода: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Произошла ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
