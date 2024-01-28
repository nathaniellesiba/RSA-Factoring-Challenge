#!/usr/bin/bash

import time
import os
import sys

# function takes single arg n and
# factor into 2 small numbers
# iterates through the range from 2 to n
# then check if n is divisible by i
# if so the it returns i and n // i, factoring n

def factorize_number(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i

# function takes file path as an args
# factor each numb in the file and writing the
# factorization in the output file
# then open output file in write mode using open function
# with the mode W and thereafter open input file to read from it

def factorize_file(file_path):
    output_file = open("output.txt", "w")

    with open(file_path, 'r') as file:
        numbers = file.readlines()

    for number in numbers:
        n = int(number)
        factors = factorize_number(n)
        output_file.write(f"{n}={factors[0]}*{factors[1]}\n")

    output_file.close()

if __name__ == "__main__":
    start_time = time.time()
    factorize_file(sys.argv[1])
    end_time = time.time()

# Check if the script ran for more than 5 seconds and delete the output file if it did
    if end_time - start_time > 5:
        os.remove("output.txt")

