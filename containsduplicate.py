class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :num_cnt:{integer:integer}
        """
        num_cnt = {}
        if nums == None:
            return False
        else:
            for element in nums:
                if not element in num_cnt:
                    num_cnt.setdefault(element,0)
                else:
                    return True
            return False

a = Solution()
print a.containsDuplicate([1,21,2])