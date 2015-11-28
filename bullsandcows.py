class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull_cnt = 0
        cow_cnt = 0
        secret_list = []
        guess_list = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_cnt += 1
            else:
                secret_list.append(secret[i])
                guess_list.append(guess[i])
        secret_list.sort()
        guess_list.sort()
        i, j = 0, 0
        while i < len(secret_list) and j < len(guess_list):
            if secret_list[i] == guess_list[j]:
                cow_cnt += 1
                i += 1
                j += 1
            elif secret_list[i] < guess_list[j]:
                i += 1
            else:
                j += 1
        return str(bull_cnt)+'A'+str(cow_cnt)+'B'

