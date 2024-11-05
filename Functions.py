class Hungarian:
    def __init__(self,matrix,size):
        self.matrix = matrix
        self.size = size
        self.matrix2 = []
        self.matrix3 = []
    
    def rowReduce(mat):
        for i in range(len(mat)):
            n = min(mat[i])
            for j in range(len(mat)):
                mat[i][j] -= n

        return mat.copy()
    
    def transpose(mat):
        tp = mat.copy()
        for i in range(len(mat)):
            tp[i] = mat[i].copy()
            for j in range(len(mat[i])):
                tp[i][j] = mat[j][i]
        
        return tp.copy()

    def colReduce(m):
        m1 = Hungarian.transpose(m)
        m2 = Hungarian.rowReduce(m1)
        m3 = Hungarian.transpose(m2)

        return m3.copy()
    
    def uniqueZero(row):
        r = row.copy()
        r.sort()
        if(r.count(0) == 1):
            return row.index(0)
        else:
            return -1
        
    def swapDi(di):
        return {v: k for k, v in di.items()}
    
    def colStrike(mat,cols,rows,di):
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
                    t2 = [x for x in range(len(m[i])) if(x not in c)]
                    z2 = t2[z]
                    c.append(z2)
                    d[i] = z2
        
        return c,r,d
    
    def rowStrike(mat,cols = [],rows = [],di = {}):
        di = di.copy()
        di = Hungarian.swapDi(di)
        r,c,d = Hungarian.colStrike(Hungarian.transpose(mat.copy()),cols = rows.copy(),rows = cols.copy(),di = di.copy())
        d = Hungarian.swapDi(d)

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
            c,r,di = Hungarian.colStrike(m,c,r,di.copy())
            c,r,di = Hungarian.rowStrike(m,c,r,di.copy())
            
            if (di2 == di):
                break

        return c,r,di2
        
    def main(self):
        di = {}
        t = 1
        while (True):
            self.matrix2 = Hungarian.rowReduce(self.matrix.copy())
            self.matrix3 = Hungarian.colReduce(self.matrix2.copy())
            c,r,di2 = Hungarian.checkBox(self.matrix2)
            di[t] = [self.matrix.copy(),self.matrix2.copy(),self.matrix3.copy(),di2.copy()]
            if(len(di2) == self.size):
                break
            else:
                self.matrix = Hungarian.subn(self.matrix3,c,r)
            
            t += 1

        return di,t