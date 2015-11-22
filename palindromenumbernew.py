class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        o = x
        ret = 0
        flag = 1
        if x < 0:
            return False
        while(x!=0):
            ret = ret*10+x%10
            x = x/10
        return ret == o