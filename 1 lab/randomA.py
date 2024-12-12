#!/usr/bin/env python3
import random
import sys

def main():
    try:
        A = random.randint(-10, 10)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"A={A}\n")
        print(A)
    except Exception as e:
        print(f"Ошибка в программе randomA: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
