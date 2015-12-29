class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x:-len(x))
        index2int = {}
        for i in range(len(words)):
            tmp = 0
            for char in words[i]:
                tmp = tmp | (1 << (ord(char) - ord('a')))
            index2int[i] = tmp

        res = 0
        for i in range(len(words)):
            if len(words[i]) * len(words[i]) <= res:
                break
            for j in range(i+1,len(words)):
                if index2int[i] & index2int[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
                    break
        return res
