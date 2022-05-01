#https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=[0]*26
        for item in magazine:
            a[ord(item)-97]+=1
        for item in ransomNote:
            a[ord(item)-97]-=1
        ans=True
        for item in a:
            if item<0:
                ans=False
        return ans