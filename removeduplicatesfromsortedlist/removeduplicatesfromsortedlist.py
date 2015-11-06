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
            preval = head.val
            curnode = head
            result = head
            while head.next != None:
                print head.val
                if head.val == preval:
                    head = head.next
                else:
                    preval = head.val
                    curnode.next = head
                    curnode = head
                    head = head.next
            if head.val == preval:
                curnode.next = None
            else:
                curnode.next = head
            return result

