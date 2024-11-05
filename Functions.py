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
    
    def colStrike(mat,cols = [],rows = [],di = {}):
        m,c,r,d = mat.copy(),cols.copy(),rows.copy(),di.copy()
        for i in range(len(m)):
            if (i in r):
                continue
            else:
                t = [m[i][x] for x in range(len(m[i])) if(x not in c)]
                z = Hungarian.uniqueZero(t)
                if(z == -1):
                    continue
                else:
                    c.append(z)
                    d[i] = z
        
        return c,r,d
    
    def rowStrike(mat,cols = [],rows = [],di = {}):
        r,c,d = Hungarian.colStrike(Hungarian.transpose(mat.copy()),cols = rows.copy,rows = cols.copy(),di = di.copy())

        return c,r,d
    
    def findn(mat,c,r):
        li = []
        for i in range(len(mat)):
            if (i not in r):
                for j in range(len(mat[i])):
                    if(j not in c):
                        li.append(mat[i][j])

        return min(li)
    
    def subn(mat,c,r):
        m = mat.copy()
        n = Hungarian.findn(m,c,r)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if(i in r and j in c):
                    m[i][j] += n
                elif(i not in r and j not in c):
                    m[i][j] -= n
        
        return m
    
    def checkBox(mat):
        c,r,di,m = [],[],{},mat.copy()
        while (True):
            di2 = di.copy()
            c,r,di = Hungarian.colStrike(m,c,r,di)
            c,r,di = Hungarian.rowStrike(m,c,r,di)
            
            if (di2 == di):
                break
        
    def main(self):
        


