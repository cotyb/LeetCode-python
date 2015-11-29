class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = 0
        result = 0
        if x < 0:
            is_negative = 1
            x = abs(x)
        while x:
            result = result * 10 + x % 10
            x /= 10
        if result >> 31 & 0xFFFFFFFF != 0:
            result = 0
        if is_negative:
            result = 0 - result

        return result