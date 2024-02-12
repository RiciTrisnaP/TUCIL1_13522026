from class_definition import *
import numpy as np
import os

def read_txt(path):
    # Membuka file 
    file = open(path,"r")

    # Buffer
    buffer = Buffer(int(file.readline())) # 1. Panjang buffer

    # Matrix
    width, height = (int(x) for x in (file.readline().split(" "))) # 2. Dimensi matriks
    matrix = Matrix(height,width)
    for i in range(height): # 3. Konten matriks
        temp = np.array(list(x for x in file.readline().rstrip('\n').split(" ") if x != ""))
        if len(temp) != width:
            print("Dimensi matrix input tidak sesuai dengan ukuran")
            exit()
        else:
            matrix.matrix[i] = temp

    # Sequences
    sequence_amount = int(file.readline()) # 4. Jumlah sekuens
    sequences = Sequences(sequence_amount)
    for i in range(sequence_amount): # 5 Token-token sekuens dan bobotnya
        temp = np.array(list(x for x in file.readline().rstrip('\n').split(" ") if x != ""))
        weight = int(file.readline())
        seq = Sequence(len(temp),weight)
        seq.list = temp
        sequences.set_element(i,seq)

    # Menutup file
    file.close

    # Mengembalikan hasil pembacaan matriks, buffer dan sekuens
    return matrix,buffer,sequences

def write_txt(max_weight, current_optimum, list_step,duration):

    # Input preferensi simpan atau tidak
    is_saved = input("Apakah ingin menyimpan solusi? (y/n): ")
    print("")
    if is_saved == "y" or "Y":
        # Input nama file .txt
        file_name = input("Masukkan nama file: ")
        path = os.path.join("../test", file_name + ".txt")
        # Open file
        with open(path,'w+') as file:
            file.write(f'{max_weight}\n')
            for x in current_optimum:
                file.write(f'{x} ')
            file.write('\n')
            for x in list_step:
                file.write(f"{x[0]} {x[1]}\n")
            file.write('\n')
            file.write(f'{duration}s')