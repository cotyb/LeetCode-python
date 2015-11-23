# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pa = headA
        pb = headB
        count = 0
        while count != 2:
            if pa == pb:
                return pa
            if pa.next:
                pa = pa.next
            else:
                count += 1
                pa = headB
            if pb.next:
                pb = pb.next
            else:
                pb = headA
        return None