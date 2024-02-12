from os.path import isfile
from random import choice

from numpy import matrix
from class_definition import *
from solution_finder import *
from random_input import *
from txt_handler import *
import os
import time


if __name__ == "__main__":
    # Prompt 
    print("==== Tipe input ====")
    print("1. Dari file .txt")
    print("2. Digenerasi secara acak")
    stop = False
    option = 0
    while not stop:
        try:
            option = int(input("Masukkan pilihan : "))
            if option != 1 and option != 2:
                raise TypeError
        except TypeError:
            print("Masukkan bilangan bulat sesuai opsi")
        else:
            stop = True
    if option == 1:
        path = input("Masukkan path file txt: ")
        if os.path.isfile(path):
            matrix,buffer,sequences = read_txt(path)
            start = time.process_time()
            print("")
            brute_forced(matrix,buffer,sequences)
            print("\n" + str(time.process_time() - start) + "s")
        else:
            print("File tidak ditemukan")
    else:
        matrix,buffer,sequences = random()
        print("\n== Matrix ==")
        matrix.print()
        print("\n== Sekuens ==")
        sequences.print()
        start = time.process_time()
        print("")
        brute_forced(matrix,buffer,sequences)
        print("\n" + str(time.process_time() - start) + "s")
    