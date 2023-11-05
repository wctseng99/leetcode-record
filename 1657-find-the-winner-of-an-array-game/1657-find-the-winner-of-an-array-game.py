class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k >= len(arr):
            return max(arr)

        count, winner = 0, None
        queue = deque(arr)
        while count < k:
            first = queue.popleft()
            second = queue.popleft()
            bigger = max(first, second)

            if winner == bigger:
                count += 1
                if count > len(arr):
                    return winner
            else:
                count = 1

            winner = bigger

            if count == k:
                return winner

            if first > second:
                queue.appendleft(first)
                queue.append(second)
            else:
                queue.appendleft(second)
                queue.append(first)

        