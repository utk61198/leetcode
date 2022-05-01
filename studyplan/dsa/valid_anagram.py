
# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        for item in s:
            a[ord(item)-97]+=1
        for item in t:
            a[ord(item)-97]-=1
        ans=True
        for item in a:
            if item!=0:
                ans=False
        return ans