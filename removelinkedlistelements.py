# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            if head.next != None:
                head = head.next
            else:
                head = None
        node = head
        while node != None and node.next != None:
            if node.next.val == val:
                if node.next.next != None:
                    node.next = node.next.next
                else:
                    node.next = None
            else:
                node = node.next
        return head


