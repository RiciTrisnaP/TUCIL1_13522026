from class_definition import *
from txt_handler import *
import numpy as np

# Inisiasi
max_weight = 0
step = 0
stop = False

def solution_finder(matrix, buffer, sequences, direction, start_position, list_step, step):
    global current_optimum # Variabel global untuk menampung sekuens optimum
    global step_optimum # Variabel global untuk menampung koordinat setiap token pada sekuens optimum
    global max_weight # Variabel global untuk menampung bobot maksimum dari sekuens optimum
    global stop # Untuk menghentikan brute force ketika terdapat sekuens yang memiliki bobot paling maksimum yang mungkin dicapai

    if not stop:
        if step != buffer.size: # Mengecek apakah buffer belum penuh
            if direction == "horizontal":
                direction = "vertical" # mengubah arah untuk step selanjutnya
                step = step + 1 # menambah counter untuk step
                for i in range(matrix.width):
                    new_position = np.copy(start_position) # membuat variabel posisi baru untuk pemanggilan fungsi rekursi selanjutnya
                    new_position[1] = i # mengubah posisi horizontal dari posisi awal
                    if matrix.get_cell(new_position[0],new_position[1]) == '##': # Skip apabila buffer mengambil token yang pernah diambil sebelumnya (invalid)
                        continue
                    list_step[step-1] = np.array([new_position[0],new_position[1]]) # Mencatat posisi dari token yang akan dimasukkan ke buffer
                    buffer.set_element(step-1,matrix.get_cell(new_position[0],new_position[1])) # Mencatat token ke dalam buffer
                    matrix.set_cell(new_position[0],new_position[1],'##') # Mengubah token yang terambil menjadi '##' (mark)
                    solution_finder(matrix, buffer, sequences, direction, new_position, list_step, step) # Rekursi
                    matrix.set_cell(list_step[step-1][0],list_step[step-1][1],buffer.get_element(step-1)) # Mengembalikan isi matriks dari mark ke token semula
                    buffer.set_element(step-1,'??') # Mengembalikan catatan buffer pada kondisi sebelumnya
                    list_step[step-1] = np.array([-1,-1]) # Menghapus posisi dari token yang dimasukkan ke buffer
            else:
                # Mirip dengan penjelasan diatas namun untuk pergerakan vertikal
                direction = "horizontal"
                step = step + 1
                for i in range(matrix.height):
                    new_position = np.copy(start_position)
                    new_position[0] = i
                    if matrix.get_cell(new_position[0],new_position[1]) == '##':  
                        continue
                    list_step[step-1] = np.array([new_position[0],new_position[1]])
                    buffer.set_element(step-1,matrix.get_cell(new_position[0],new_position[1]))
                    matrix.set_cell(new_position[0],new_position[1],'##')
                    solution_finder(matrix, buffer, sequences, direction, new_position, list_step, step)
                    matrix.set_cell(list_step[step-1][0],list_step[step-1][1],buffer.get_element(step-1))
                    buffer.set_element(step-1,'??')
                    list_step[step-1] = np.array([-1,-1])
        else:
            weight = sequences.match_all(buffer.list) # Mencocokkan buffer dengan sekuens dan menyimpan hasil evaluasi bobotnya
            if weight > max_weight: # Mengecek apakah bobot maksimum dan mencatat step dan sekuen token-tokennya
                max_weight = weight
                step_optimum = list_step.tolist()
                current_optimum = np.copy(buffer.list)
                if max_weight == sequences.get_max_weight(): # Menghentikan bruteforce ketika bobot maksimum tercapai
                    stop = True
                    for i in range(sequences.get_element(0).size,buffer.size): # Mencari step paling sedikit ketika ditemukan bobot maksimum
                        temp =  current_optimum[:i]
                        weight = sequences.match_all(temp)
                        if weight == max_weight:
                            current_optimum = temp
                            step_optimum = step_optimum[:i]
                            break



def brute_forced(matrix,buffer,sequences):
    global current_optimum
    global step_optimum

    # Inisiasi
    direction = "horizontal"
    start_position = np.array([0,0])
    step_optimum = []
    list_step = np.full([buffer.size,2],-1)
    current_optimum = np.full([buffer.size], '??')

    # Brute force solusi
    solution_finder(matrix,buffer,sequences,direction,start_position,list_step,step)

    # Output hasil
    print(max_weight)
    if current_optimum[0] != '??':
        for x in current_optimum:
            print(f"{x} ",end="")
        print("")
        for x in step_optimum:
            print(f"{x[0]} {x[1]}")
    else:
        print("Tidak ada solusi")