# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            p = head
            while p.next != None:
                if p.next.val == p.val:
                    p.next = p.next.next
                else:
                    p = p.next

