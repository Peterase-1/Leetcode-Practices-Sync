class Solution(object):
    def escapeGhosts(self, ghosts, target):
        my_dist = abs(target[0]) + abs(target[1])

        for gx, gy in ghosts:
            ghost_dist = abs(gx - target[0]) + abs(gy - target[1])
            if ghost_dist <= my_dist:
                return False

        return True
