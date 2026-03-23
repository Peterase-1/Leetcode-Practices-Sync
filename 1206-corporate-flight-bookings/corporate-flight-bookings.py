class Solution(object):
    def corpFlightBookings(self, b, n):
        a = [0] * n

        for x in b:
            l = x[0] - 1
            r = x[1] - 1
            v = x[2]

            a[l] += v
            if r + 1 < n:
                a[r + 1] -= v

        for i in range(1, n):
            a[i] += a[i - 1]

        return a