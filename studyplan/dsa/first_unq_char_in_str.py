# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][1]+=1
            else:
                d[s[i]]=[i,1]
        m=float('inf')
        for key in d:
            if d[key][1]==1 and d[key][0]<m:
                m=d[key][0]
        if m==float('inf'):
            return -1
        else:
            return m