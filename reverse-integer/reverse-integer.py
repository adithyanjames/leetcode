class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = x < 0
        rev = 0
        x = abs(x)
        while x > 0:
            rev *= 10
            rev += x % 10
            x /= 10
        if rev > 1<<31:
            return 0

        if isNegative:
            return rev*-1
        else:
            return rev