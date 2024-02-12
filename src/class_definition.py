import numpy as np
class Matrix:
    def __init__(self,height,width):
        self.width = width
        self.height = height
        self.matrix = np.full([height,width], '??')

    def print(self):
        print(self.matrix)
    
    def get_cell(self,row,column):
        return(self.matrix[row,column])
    
    def set_cell(self,row,column,value):
        self.matrix[row,column] = value
    
    def copy(self):
        matrix_cp = Matrix(self.height, self.width)
        matrix_cp.matrix = np.copy(self.matrix)
        return matrix_cp

class Buffer:
    def __init__(self,size):
        self.size = size
        self.list = np.full([size], '??')

    def print(self):
        print(self.list)
    
    def get_element(self,idx):
        return(self.list[idx])
    
    def set_element(self,idx,value):
       self.list[idx] = value

class Sequence:
    def __init__(self,size,weight):
        self.size = size
        self.weight = weight
        self.list = np.full([size], '??')

    def __repr__(self):
        return np.array2string(self.list)

    def __str__(self):
        return np.array2string(self.list)

    def print(self):
        print(np.array2string(self.list))

    def get_element(self,idx):
        return(self.list[idx])
    
    def set_element(self,idx,value):
        self.list[idx] = value

    def match(self,list):
        length = self.size
        for i in range(length):
            temp = list[i:i+length]
            if np.array_equal(self.list, temp):
                return self.weight
        return 0

class Sequences:
    def __init__(self,size):
        self.size = size
        self.list = np.full([size], Sequence(2,0))

    def print(self):
        print(self.list)
        print(f'weight : {list(x.weight for x in self.list)}')

    def get_element(self,idx):
        return(self.list[idx])
    
    def set_element(self,idx,value):
        self.list[idx] = value

    def get_max_weight(self):
        sum = 0
        for x in self.list:
            sum += x.weight
        return sum

    def match_all(self,list):
        sum = 0
        for sequence in self.list:
            sum += sequence.match(list)
        return sum

