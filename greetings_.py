#!/usr/bin/env python3
import re
import sys


# Функция проверки имени
def is_valid_name(name):
    return bool(re.match(r"^[A-Z][a-zA-Z]*$", name))


def greet(name):
    print(f"Привет, {name}!")


# Режим 1:
def greet_from_file(filename):
    try:
        with open(filename, "r") as file:
            names = file.readlines()

        with open("error.txt", "w") as error_file:
            for name in names:
                name = name.strip()
                if is_valid_name(name):
                    greet(name)
                else:
                    error_file.write(f"Ошибка: Некорректное имя '{name}'\n")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.", file=sys.stderr)
    except Exception as e:
        print(f"Произошла ошибка: {e}", file=sys.stderr)


# Режим 2
def greet_interactive():
    try:
        while True:
            name = input("Введите имя: ").strip()
            if is_valid_name(name):
                greet(name)
            else:
                print("Ошибка: Некорректное имя. Имя должно начинаться с заглавной буквы и содержать только буквы.")
    except KeyboardInterrupt:
        print("\nДо свидания!")
    except Exception as e:
        print(f"Произошла ошибка: {e}", file=sys.stderr)


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        greet_from_file(filename)
    else:
        greet_interactive()


if __name__ == "__main__":
    main()