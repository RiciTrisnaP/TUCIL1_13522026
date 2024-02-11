import numpy as np

class Token:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value

class Matrix:
    def __init__(self,height,width):
        self.width = width
        self.height = height
        self.matrix = np.full([height,width], Token('00'))

    def print(self):
        print(self.matrix)
    
    def get_cell(self,row,column):
        return(self.matrix[row,column])
    
    def set_cell(self,row,column,value):
        self.matrix[row,column] = value

class Buffer:
    def __init__(self,size):
        self.size = size
        self.list = np.full([size], Token('00'))

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
        self.list = np.full([size], Token('00'))

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

    def match(self,buffer):
        length = self.size
        for i in range(length):
            temp = buffer.list[i:i+length]
            if np.array_equal(self.list,temp):
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

    def match_all(self,buffer):
        sum = 0
        for sequence in self.list:
            sum += sequence.match(buffer)
        return sum