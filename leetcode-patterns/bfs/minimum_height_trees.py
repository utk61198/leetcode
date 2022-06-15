

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [i for i in range(n)]
        graph = [[] for _ in range(n)]
        degree = [0]*n


        # calculating the in degrees of the nodes
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        queue = []
        # adding the leaf nodes to the queue
        for idx, val in enumerate(degree):
            if val == 1:
                queue.append(idx)

        while n > 2:
            q_len = len(queue)
            n = n - q_len
            for i in range(q_len):
                popped = queue.pop(0)
                #decrementing the leafnode's neighbors degrees by 1 ( basically removing leadnode)
                for neighbor in graph[popped]:
                    degree[neighbor] = degree[neighbor] - 1
                    # adding the new leaf nodes to the queue
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return queue


if __name__ == '__main__':
    obj = Solution()
    print(obj.findMinHeightTrees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]))
