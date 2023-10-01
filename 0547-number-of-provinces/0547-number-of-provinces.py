class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            for neighbor in range(len(isConnected[city])):
                if neighbor not in cities and isConnected[city][neighbor]  == 1:
                    cities.add(neighbor)
                    dfs(neighbor)

        province = 0
        cities = set()

        for node in range(len(isConnected)):
            if node not in cities:
                cities.add(node)
                province += 1
                dfs(node)
        return province