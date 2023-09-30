class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(room):
            while room:
                number = room.pop()
                unlock[number] = True
                dfs(rooms[number])

        unlock = [False] * len(rooms)
        unlock[0] = True
        dfs(rooms[0])
        
        return True if all(unlock) else False


        
            