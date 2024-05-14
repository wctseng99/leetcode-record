"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue, graph = deque([node]), {node.val: Node(node.val)}

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val not in graph:
                    graph[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                graph[cur.val].neighbors.append(graph[neighbor.val])
        return graph[node.val]