from class_definition import *
from random import uniform, randint, randrange
import numpy as np

def random():

    # Token
    token_count = int(input()) # 1. Jumlah token unik
    tokens = np.array(list(x for x in input().rstrip('\n').split(" ") if x != "")) # 2. Token unik ex: BD E9 1C 2D 33
    if len(tokens) != token_count:
        print("Jumlah token tidak sesuai dengan inputan !!")
        exit() # Keluar ketika input tidak sesuai

    # Buffer
    buffer_size = int(input()) # 3. Ukuran buffer
    buffer = Buffer(buffer_size)

    # Matrix
    width, height = (int(x) for x in (input().split(" "))) # 4. Width dan height matriks
    matrix = Matrix(height,width)
    generate_random_matrix(matrix,tokens)

    # Sequence
    sequence_count = int(input()) # 5. Jumlah sequence 
    sequences = Sequences(sequence_count)
    sequence_max_len = int(input()) # 6. Panjang maksimal sequence
    generate_random_sequences(sequences,sequence_count,sequence_max_len,tokens)

    return matrix, buffer, sequences

def generate_random_matrix(matrix,tokens):
    for i in range(matrix.height):
        for j in range(matrix.width):
            matrix.set_cell(i,j,tokens[randint(0, len(tokens)-1)]) # Mengambil token random untuk mengisi setiap sel pada matriks

def generate_random_sequences(sequences,sequence_count,sequence_max_len,tokens):
    listlen = [] # list untuk menampung beberapa bilangan bulat hasil randomisasi yang digunakan sebagai panjang setiap sekuens
    listweight = [] # mirip listlen namun digunakan untuk bobot tiap sekuens
    for i in range(sequence_count):
        listlen.append(randintskew(2,sequence_max_len,uniform(1,2))) # mengenerasi bilangan bulat acak yang condong ke arah lower bound
        listweight.append(randrange(10,100,5)) # mengenerasi bilangan bulat acak keliapatan lima antara 10 dan 100
    # Menyortir list 
    listlen.sort() 
    listweight.sort() 

    for i,x in enumerate(listlen): # Mengenerasi sekuens sesuai panjang dan bobot yang dirandomisasi sebelumnya
        temp = Sequence(x, listweight[i])
        for j in range(x):
            temp.list[j] = tokens[randint(0, len(tokens)-1)]
        sequences.set_element(i,temp)

def randintskew(min,max,power): # Fungsi untuk mengenerasi bilangan yang condong ke arah lower bound
        seed = uniform(0,1)
        pos = pow(seed,power)
        return int(round((max - min) * pos + min))

def rapidrandintskew(min,max,power,time): 
    sum = 0
    for i in range(time): # melakukan generasi bilangan bulat sebanyak variabel time
        temp = randintskew(min,max,power)
        sum += temp
    avr = round(sum / time) # Mencari average pada beberapa hasil generasi bilangan bulat yang condong ke arah lower bound
    return avr # Mengambil rata-rata sebagai hasil randomisasi