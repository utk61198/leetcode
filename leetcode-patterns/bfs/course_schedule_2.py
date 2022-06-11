# https://leetcode.com/problems/course-schedule-ii/


from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course_pair in prerequisites:
            graph[course_pair[1]].append(course_pair[0])
        ans = []
        visited = [0]*numCourses
        def topological_sort(node):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
            visited[node] = -1
            for neighbor in graph[node]:
                if topological_sort(neighbor):
                    return True
            visited[node] = 1
            ans.append(node)
            return False
        for neighbor in range(numCourses):
            if topological_sort(neighbor):
                return []
        return ans[::-1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(obj.findOrder(2, [[1, 0]]))
    print(obj.findOrder(6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]))
