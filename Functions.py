class Hungarian:
    def __init__(self,matrix):
        self.matrix = matrix
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
    
    def uniqueZero(row):
        r = row.copy()
        r.sort()
        if(r[0] == r[1]):
            return -1
        else:
            return row.index(0)
    
    def colStrike(mat,cols = [],di = {}):
        m,c,d = mat.copy(),cols.copy(),di.copy()
        for i in m:
            z = Hungarian 


        
