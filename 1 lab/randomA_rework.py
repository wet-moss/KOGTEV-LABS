#!/usr/bin/env python3
import random

def main():
    A = random.randint(-10, 10)
    print(A)
    with open("output.txt", "a") as output_file:
        output_file.write(f"A = {A}\n")

if __name__ == "__main__":
    main()
