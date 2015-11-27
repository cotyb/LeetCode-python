class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        while n - 1:
            tmp = ''
            list = []
            for i in range(len(result)):
                if not list:
                    list.append(result[i])
                else:
                    if result[i] == list[-1]:
                        list.append(result[i])
                    else:
                        tmp += str(len(list)) + list[-1]
                        list = []
                        list.append(result[i])
                if i == len(result) - 1:
                    tmp += str(len(list)) + list[-1]
            result = tmp
            n -= 1
        return result
so = Solution()
print so.countAndSay(5)

