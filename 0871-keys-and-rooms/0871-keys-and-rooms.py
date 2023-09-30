class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(room):
            while room:
                number = room.pop()
                unlock.add(number)
                dfs(rooms[number])

        unlock = set()
        unlock.add(0)
        dfs(rooms[0])
        
        return True if len(unlock) == len(rooms) else False


        
            