class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a = (len_b - len_a)*'0' + a
        else:
            b = (len_a - len_b)*'0' + b
        c = 0
        result = ''
        for i in range(len(a))[::-1]:
            if ord(a[i]) - ord('0') + ord(b[i]) - ord('0') + c == 3:
                result = '1' + result
                c = 1
            elif ord(a[i]) - ord('0') + ord(b[i]) - ord('0') + c == 2:
                result = '0' + result
                c = 1
            else:
                result = str(ord(a[i]) - ord('0') + ord(b[i]) - ord('0') + c) + result
                c = 0
        if c == 1:
            result = '1' + result
        return result
