#!/usr/bin/env python3
import re
import sys

def is_valid_name(name):
    return bool(re.match(r"^[A-Z][a-zA-Z]*$", name))

def greet_from_file(filename):
    try:
        with open(filename, "r") as file, open("error.txt", "w") as error_file:
            for line in file:
                name = line.strip()
                if is_valid_name(name):
                    print(f"Привет, {name}!")
                else:
                    error_file.write(f"Некорректное имя: {name}\n")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.", file=sys.stderr)

def greet_interactive():
    try:
        while True:
            name = input("Введите имя: ").strip()
            if is_valid_name(name):
                print(f"Привет, {name}!")
            else:
                print("Некорректное имя. Имя должно начинаться с заглавной буквы и содержать только буквы.", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nДо свидания!")

def main():
    if len(sys.argv) > 1:
        greet_from_file(sys.argv[1])
    else:
        greet_interactive()

if __name__ == "__main__":
    main()
