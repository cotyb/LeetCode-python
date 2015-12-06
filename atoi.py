class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag = 1
        length = len(str)
        i = 0
        result = 0
        while i < length and str[i] == ' ':
            i += 1
        if i == length:
            return 0
        elif str[i] == "+":
            flag = 1
            i += 1
        elif str[i] == "-":
            flag = -1
            i += 1
        if i == length:
            return 0
        if not (str[i] <= '9' and str[i] >= '0'):
            return 0
        else:
            str = str[i:]
        for i in range(len(str)):
            if str[i] <= '9' and str[i] >= '0':
                result = result * 10 + ord(str[i]) - ord('0')
            else:
                break
        if flag == -1:
            if -1 * result <= -2147483648:
                return  -2147483648
        else:
            if result > 2147483647:
                result = 2147483647
        return flag * result


so = Solution()
print so.myAtoi("-2147483648")