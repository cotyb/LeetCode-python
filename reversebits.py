class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            tail = n & 1
            result |= tail
            n >>= 1
        return result

so = Solution()
print so.reverseBits( 1)