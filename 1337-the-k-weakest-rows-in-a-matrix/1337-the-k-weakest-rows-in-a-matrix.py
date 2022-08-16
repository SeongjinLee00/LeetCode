class Solution:
    def kWeakestRows(self, mat, k):
        arr=[]
        for i in range(len(mat)):
            arr.append([sum(mat[i]),i])
        
        arr.sort()
        tmp=[]

        for j in range(k):
            tmp.append(arr[j][1])

        return tmp