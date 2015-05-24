class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dictMap={};   #dict的查找速度不会随着元素的增多而变慢
        for index,value in enumerate(nums):
            if target-value in dictMap:
                return dictMap[target-value]+1,index+1
            dictMap[value]=index   #将已经遍历过的元素按照value-index进行存储