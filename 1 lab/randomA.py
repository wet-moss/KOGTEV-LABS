#!/usr/bin/env python3
import random
import sys

def main():
    try:
        # Генерация случайного числа A
        A = random.randint(-10, 10)
        
        # Записываем значение A в logs.txt
        with open("logs.txt", "a") as log_file:
            log_file.write(f"A={A}\n")
        
        # Выводим значение A на консоль
        print(A)
    except Exception as e:
        print(f"Ошибка в программе randomA: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
