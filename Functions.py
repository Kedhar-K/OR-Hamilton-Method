class Hungarian:
    def __init__(self,matrix):
        self.matrix = matrix
        self.size = len(matrix)
        self.matrix2 = []
        self.matrix3 = []
    
    def rowReduce(self, mat):
        self.matrix2 = mat.copy()
        for i in range(self.size):
            for j in range(self.size):
                self.matrix2[i][j] = self.matrix[i][j] - min(self.matrix[i])

        return self.matrix2.copy()
    
    def transpose(self):
        tp = self.matrix2.copy()
        for i in range(self.size):
            for j in range(self.size):
                tp[i][j] = self.matrix[j][i]
        
        return tp.copy()

    def colReduce(self):
        for n in range(self.size):
            res = [min(i) for i in zip(*self.matrix)][n]
            self.matrix3 = self.matrix2.copy()
            for j in range(self.size):
                self.matrix3[j][n] = self.matrix3[j][n] - res
        

import os
print(os.getcwd())