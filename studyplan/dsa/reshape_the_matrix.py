#https://leetcode.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c==len(mat)*len(mat[0]):
            a=[]
            b=[]
            for items in mat:
                for item in items:
                    b.append(item)
                    if len(b)==c:
                        a.append(b)
                        b=[] 
            return a
        else:
            return mat
            
        