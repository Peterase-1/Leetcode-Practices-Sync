class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transposed = []

        for j in range(len(matrix[0])):
            new_row = [] 

            for i in range(len(matrix)):
                new_row.append(matrix[i][j])

            transposed.append(new_row)

        return transposed
