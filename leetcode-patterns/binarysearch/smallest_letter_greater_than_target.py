 # https://leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0 
        high = len(letters) - 1
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] == target:
                if mid == len(letters)-1 and letters[mid] != letters[0]:
                    return letters[0]
                elif letters[mid] != letters[mid+1]:
                    return letters[mid+1]
                else:
                    low = mid + 1
            elif letters[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return letters[0] if low >= len(letters) else letters[low]
        