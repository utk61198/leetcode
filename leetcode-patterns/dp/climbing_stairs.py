
# https://leetcode.com/problems/climbing-stairs/
class Solution:
	def climbStairs(self, n: int) -> int:
		# recursive solution
        # if n<0:
        #     return 0
        # if n == 0:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        arr = [0]*(n+1)
        def climb(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if arr[n] != 0:
                return arr[n]
            arr[n] = climb(n-1) + climb(n-2)
            return arr[n]
        
        return climb(n)





if __name__ == '__main__':
	obj = Solution()
	print(obj.climbStairs(3)) 