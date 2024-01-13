class Solution(object):
    def divide(self, A, B):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # count = 0
        # curr = dividend

        # while curr >= abs(divisor):
        #     curr = dividend - abs(divisor)
        #     count += 1

        # if divisor < 0:
        #     return -1 * count

        # else:
        #     return count
        if (A == -2147483648 and B == -1):
            return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res
