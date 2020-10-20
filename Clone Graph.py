# Done
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        references = {1: Node(1)}

        def dfs(copy_from):
            for n in copy_from.neighbors:
                value = n.val
                if value not in references:
                    references[value] = Node(value, [references[copy_from.val]])
                    dfs(n)
                else:
                    if references[copy_from.val] not in references[value].neighbors:
                        references[value].neighbors.append(references[copy_from.val])

        dfs(node)
        return references[1]