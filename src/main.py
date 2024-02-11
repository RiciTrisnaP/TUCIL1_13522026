from class_definition import *
from solution_finder import *
from random_input import *
from txt_handler import *


matrix,buffer,sequences = read_txt("test.txt")
matrix_cp = matrix.copy()
current_optimum = np.full([buffer.size], '??')
step_optimum = []
list_step = np.full([buffer.size,2],-1)
start_position = np.array([0,0])
direction = "horizontal"
max_weight = 0
step = 0

brute_forced(matrix,buffer,sequences,direction,start_position,list_step,step)