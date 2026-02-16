class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        reverse = []
        invert = []
        for i in image:
            reverse.append(i[::-1])
        for i in reverse:
            new_row = []
            for j in i:
                if j ==0:
                    new_row.append(1)
                else:
                    new_row.append(0)
            invert.append(new_row)
        return invert