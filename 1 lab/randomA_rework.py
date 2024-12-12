#!/usr/bin/env python3
import random

def main():
    A = random.randint(-10, 10)
    print(A)
    with open("logs.txt", "a") as log_file:
        log_file.write(f"A={A}\n")

if __name__ == "__main__":
    main()
