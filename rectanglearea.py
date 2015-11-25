class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area = (D - B) * (C - A) + (G - E) * (H - F)
        A1, B1, C1, D1 = max(A,E), max(B,F), min(C,G), min(D,H)
        if H <= B or F >= D or E >= C or G <= A:
            return total_area
        return total_area - (C1 - A1) * (D1 - B1)