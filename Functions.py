class Hungarian:
    def __init__(self,matrix):
        self.matrix = matrix
        self.size = len(matrix)
        self.matrix2 = []
        self.matrix3 = []
    
    def rowReduce(mat):
        m = mat.copy()
        for i in range(len(m)):
            n = min(mat[i])
            m[i] = [x - n for x in m[i]]

        return m.copy()
    
    def transpose(mat):
        tp = mat.copy()
        for i in range(len(mat)):
            for j in range(len(mat)):
                tp[i][j] = mat[j][i]
        
        return tp.copy()

    def colReduce(mat):
        m = mat.copy()
        m = Hungarian.transpose(m)
        m = Hungarian.rowReduce(m)
        m = Hungarian.transpose(m)

        return m.copy
    

        
