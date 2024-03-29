class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i, u, w in times:
            graph[i].append((u, w))
        
        visited = set()
        distances = {node: float('inf') for node in range(1, n+1)}
        
        distances[k] = 0
        
        while len(visited) != n:
            # Find the node with the smallest distance
            min_dis = float('inf')
            min_node = None
            
            for node in range(1, n+1):
                if node not in visited and distances[node] < min_dis:
                    min_node = node
                    min_dis = distances[node]
                    
            if min_node is None:
                break
            
            # Mark the node as visited
            visited.add(min_node)
            
            # Update distances to neighboring nodes
            for neighbor, time in graph[min_node]:
                distance = min_dis + time
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
            
        return max(distances.values()) if len(visited) == n else -1