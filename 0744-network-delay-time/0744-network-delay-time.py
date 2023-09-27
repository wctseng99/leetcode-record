class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0
        visited = set()

        for u, v, w in times:
            graph[u].append((v, w))

        while len(visited) < n:
            min_node = None
            min_dist = float('inf')
            # find the node with the minimum distance
            for node in range(1, n+1):
                if node not in visited and distances[node] < min_dist:
                    min_node = node
                    min_dist = distances[node]
            if min_node is None:
                break
            visited.add(min_node)
            # update the distances
            for v, w in graph[min_node]:
                distances[v] = min(distances[v], distances[min_node] + w)
        return max(distances.values()) if len(visited) == n else -1