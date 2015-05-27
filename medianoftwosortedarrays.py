class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        nums1.append(float("inf"))
        n = len(nums2)
        nums2.append(float("inf"))
        result1 = []
        result2 = []
        i = 0
        j = 0
        result = 0
        if (m + n) % 2 == 1:
            while (i + j) < (m+n)/2 + 1:
                if nums1[i] <= nums2[j]:
                   result1.append(nums1[i])
                   i += 1
                else:
                   result1.append(nums2[j])
                   j += 1
            result = result1[(m + n)/2]
        else:
            while (i + j) < (m+n)/2 + 1:
                if nums1[i] <= nums2[j]:
                   result2.append(nums1[i])
                   i += 1
                else:
                   result2.append(nums2[j])
                   j += 1
            result = (result2[(m + n)/2-1] + result2[(m+n)/2])/2.0
        return result