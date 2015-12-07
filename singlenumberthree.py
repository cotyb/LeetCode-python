class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        for ele in nums:
            tmp = ele ^ tmp
        i = 0
        while tmp & 1 == 0:
            i += 1
            tmp = tmp >> 1
        list1 = []
        list2 = []
        for ele in nums:
            if (ele >> i) & 1 == 1:
                list1.append(ele)
            else:
                list2.append(ele)
        tmp1, tmp2 = 0, 0
        for ele in list1:
            tmp1 = tmp1 ^ ele
        for ele in list2:
            tmp2 = tmp2 ^ ele
        return [tmp1,tmp2]

so = Solution()
print so.singleNumber([0,0,1,2])