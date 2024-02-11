from class_definition import *
from random import uniform, randint, randrange
import numpy as np

def random(path):
    # Open file in path
    file = open(path,"r")

    # Token
    token_count = int(file.readline()) # 1. Jumlah token unik
    tokens = np.array(list(x for x in file.readline().rstrip('\n').split(" ") if x != "")) # 2. Token unik ex: BD E9 1C 2D 33
    if len(tokens) != token_count:
        print("Jumlah token tidak sesuai dengan inputan !!")
        exit() # Keluar ketika input tidak sesuai

    # Buffer
    buffer_size = int(file.readline()) # 3. Ukuran buffer
    buffer = Buffer(buffer_size)

    # Matrix
    width, height = (int(x) for x in (file.readline().split(" "))) # 4. Width dan height matriks
    matrix = Matrix(height,width)
    generate_random_matrix(matrix,tokens)

    # Sequence
    sequence_count = int(file.readline()) # 5. Jumlah sequence 
    sequences = Sequences(sequence_count)
    sequence_max_len = int(file.readline()) # 6. Panjang maksimal sequence
    generate_random_sequences(sequences,sequence_count,sequence_max_len,tokens)

    # Close file
    file.close
    return matrix, buffer, sequences

def generate_random_matrix(matrix,tokens):
    for i in range(matrix.height):
        for j in range(matrix.width):
            matrix.set_cell(i,j,tokens[randint(0, len(tokens)-1)]) # Mengambil token random untuk mengisi setiap sel pada matriks

def generate_random_sequences(sequences,sequence_count,sequence_max_len,tokens):
    listlen = []
    listweight = []
    for i in range(sequence_count):
        listlen.append(rapidrandintskew(2,sequence_max_len,uniform(1,4),20))
        listweight.append(randrange(10,100,5))
    listlen.sort()
    listweight.sort()

    for i,x in enumerate(listlen):
        temp = Sequence(x, listweight[i])
        for j in range(x):
            temp.list[j] = tokens[randint(0, len(tokens)-1)]
        sequences.set_element(i,temp)

def rapidrandintskew(min,max,power,time): # Fungsi untuk mengenerasi bilangan yang condong ke arah minimum

    def randintskew(min,max,power):
        seed = uniform(0,1)
        pos = pow(seed,power)
        return int(round((max - min) * pos + min))

    sum = 0
    for i in range(time):
        temp = randintskew(min,max,power)
        sum += temp
    avr = round(sum / time)
    return avr