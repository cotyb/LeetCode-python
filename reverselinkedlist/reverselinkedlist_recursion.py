# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            next_node = head.next
            new_head = self.reverseList(next_node)
            head.next = None
            next_node.next = head
        return new_head



