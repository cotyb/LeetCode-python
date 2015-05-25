# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        first,carry = ListNode(0), 0
        head = first
        while carry or l1 or l2:
            node = ListNode(carry)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            carry = node.val / 10
            node.val = node.val % 10
            head.next = node
            head = head.next
        return first.next