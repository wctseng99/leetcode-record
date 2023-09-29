class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0
        visited = set()

        for u, v, w in times:
            graph[u].append((v, w))
        
        while len(visited) != n:
            # Find the node with the smallest distance
            min_node = None
            min_distance = float('inf')
            for node in distances:
                if distances[node] < min_distance and node not in visited:
                    min_node = node
                    min_distance = distances[node]
            
            if not min_node:
                break
            # Mark it as visited
            visited.add(min_node)

            # Update the the distances of neighbor nodes
            for neighbor, times in graph[min_node]:
                distances[neighbor] = min(distances[neighbor], (distances[min_node] + times))

        return max(distances.values()) if len(visited) == n else -1