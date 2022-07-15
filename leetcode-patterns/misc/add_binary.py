# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        c = 0
        ans = ''
        while a or b or c:
            if a:
                c = c + int(a.pop())
            if b:
                c = c + int(b.pop())
            ans = ans + str(c%2)
            c = c // 2
        return ans[::-1]
        