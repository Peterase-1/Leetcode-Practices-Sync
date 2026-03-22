class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.st = []
            return
        
        r = len(matrix)
        c = len(matrix[0])
        

        self.st = [[0] * (c + 1) for _ in range(r + 1)]
        
        for i in range(r):
            for j in range(c):
                self.st[i+1][j+1] = (
                    matrix[i][j]
                    + self.st[i][j+1]
                    + self.st[i+1][j]
                    - self.st[i][j]
                )

    def sumRegion(self, r1, c1, r2, c2):
        return (
            self.st[r2+1][c2+1]
            - self.st[r1][c2+1]
            - self.st[r2+1][c1]
            + self.st[r1][c1]
        )