class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dummy_index = len(digits) - 1
        digits[-1] += 1
        while dummy_index > 0:
            if digits[dummy_index] > 9:
                digits[dummy_index] -= 10
                digits[dummy_index-1] += 1
            dummy_index -= 1
        if digits[0] > 9:
            digits[0] -= 10
            digits.insert(0,1)
        return digits

a = Solution()
print a.plusOne([9,9,9,9])


