class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), w in zip(edges, succProb):
            # undirected edge
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited = set()
        # using heap to handle the min probability
        heap = [[-1, start_node]]

        while heap:
            path_prob, node = heappop(heap)
            # heappop to find the min prob
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return -path_prob
            for neighbor, prob in graph[node]:
                heappush(heap, [prob * path_prob, neighbor]) 
        return 0
