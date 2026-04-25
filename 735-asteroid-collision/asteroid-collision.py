class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:

            current = ast

            while True:

                if not stack or current > 0 or stack[-1] < 0:
                    stack.append(current)
                    break

                top = stack[-1]

                if top < -current:
                    stack.pop()      
                    continue

                elif top == -current:
                    stack.pop()      
                    break

                else:

                    break

        return stack