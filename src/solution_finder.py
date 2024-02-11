from class_definition import *
from txt_handler import *
import numpy as np

max_weight = 0

def solution_finder(matrix, buffer, sequences, direction, start_position, list_step, step):
    global current_optimum 
    global step_optimum
    global max_weight
    if step != buffer.size:
        if direction == "horizontal":
            direction = "vertical"
            step = step + 1
            for i in range(matrix.width):
                new_position = np.copy(start_position)
                new_position[1] = i
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
        weight = sequences.match_all(buffer)
        if weight > max_weight:
            max_weight = weight
            step_optimum = list_step.tolist()
            current_optimum = np.copy(buffer.list)


def brute_forced(matrix,buffer,sequences,direction,start_position,list_step,step):
    solution_finder(matrix,buffer,sequences,direction,start_position,list_step,step)
    print(max_weight)
    for x in current_optimum:
        print(f"{x} ",end="")
    print("")
    for x in step_optimum:
        print(f"{x[0]} {x[1]}")