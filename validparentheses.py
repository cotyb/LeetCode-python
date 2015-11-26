class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        for char in s:
            if char in ['(','{','[']:
                list.append(char)
            elif char == '}':
                if len(list) == 0:
                    return False
                if list.pop() != '{':
                    return False
            elif char == ']':
                if len(list) == 0:
                    return False
                if list.pop() != '[':
                    return False
            else:
                if len(list) == 0:
                    return False
                if list.pop() != '(':
                    return False
        if len(list) != 0:
            return False
        return True



