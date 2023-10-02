class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] > -i:
                    i = 0
                elif stack[-1] < -i:
                    stack.pop()
                else:
                    stack.pop()
                    i = 0
            if i:
                stack.append(i)
        return stack