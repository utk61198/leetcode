
# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course_pair in prerequisites:
            graph[course_pair[0]].append(course_pair[1])

        node_state = [0]*numCourses

        def has_cycle(node):
            if node_state[node] == -1:
                return True
            if node_state[node] == 1:
                return False

            node_state[node] = -1

            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            node_state[node] = 1
            return False

        for course_node in range(numCourses):
            if has_cycle(course_node):
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
