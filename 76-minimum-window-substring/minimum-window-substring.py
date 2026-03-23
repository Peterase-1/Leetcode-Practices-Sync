class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        n = {}
        for c in t:
            n[c] = n.get(c, 0) + 1

        w = {}
        h = 0
        nd = len(n)

        l = 0
        ml = float("inf")
        res = ""

        for r in range(len(s)):
            c = s[r]
            w[c] = w.get(c, 0) + 1

            if c in n and w[c] == n[c]:
                h += 1

            while h == nd:
                if (r - l + 1) < ml:
                    ml = r - l + 1
                    res = s[l:r+1]

                lc = s[l]
                w[lc] -= 1

                if lc in n and w[lc] < n[lc]:
                    h -= 1

                l += 1

        return res