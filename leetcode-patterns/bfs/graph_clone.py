
# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        q = [node]
        # create a copy dictionary to track the visisted nodes & this will only keep copy nodes
        copy = {node.val: Node(node.val)}

        while q:
            original_pop = q.pop(0)

            # original grah element popped from the queue
            # create a new node and assign value from the copy dict
            new_node = copy[original_pop.val]
            for item in original_pop.neighbors:        # traverse neighbors of original popped
                # if neighbor not in copy, create a new node and add in copy.
                if item.val not in copy:
                    copy[item.val] = Node(item.val)
                    # append the neighbor of original popped to carry on BFS
                    q.append(item)
                # also add the created copy to neighbors of the current copy node
                new_node.neighbors.append(copy[item.val])
        return copy[node.val]
