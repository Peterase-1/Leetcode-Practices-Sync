from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True