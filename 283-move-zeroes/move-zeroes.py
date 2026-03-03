class Solution(object):
    def moveZeroes(self, arr):
        sl = 0

        for ft in range(len(arr)):
            if arr[ft] !=0:
                arr[sl] = arr[ft]
                sl+=1

        for i in range(sl,len(arr)):
            arr[i]=0