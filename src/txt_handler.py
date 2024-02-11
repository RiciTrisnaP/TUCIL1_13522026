from class_definition import *
import numpy as np

def read_txt(path):
    file = open(path,"r")
    buffer = Buffer(int(file.readline()))
    width, height = (int(x) for x in (file.readline().split(" ")))
    matrix = Matrix(height,width)
    for i in range(height):
        temp = np.array(list(x for x in file.readline().rstrip('\n').split(" ") if x != ""))
        if len(temp) != width:
            print("Dimensi matrix input tidak sesuai dengan ukuran")
            exit()
        else:
            matrix.matrix[i] = temp
    sequence_amount = int(file.readline())
    sequences = Sequences(sequence_amount)
    for i in range(sequence_amount):
        temp = np.array(list(x for x in file.readline().rstrip('\n').split(" ") if x != ""))
        weight = int(file.readline())
        seq = Sequence(len(temp),weight)
        seq.list = temp
        sequences.set_element(i,seq)
    file.close
    return matrix,buffer,sequences