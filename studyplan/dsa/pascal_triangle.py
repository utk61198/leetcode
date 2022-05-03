
# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        for l in range(1,numRows+1):
            t=[]
            x=1
            for i in range(1,l+1):
                t.append(x)
                x=int(x*(l-i)/i)
            a.append(t)
        return a