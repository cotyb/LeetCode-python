#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = n
        if not head:
            return None
        tmp = head
        result = head
        while n and tmp.next:
            tmp = tmp.next
            n -= 1
        while tmp.next:
            head = head.next
            tmp = tmp.next
        if n == 1:
            result = result.next
        else:
            head.next = head.next.next
        return result

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
so = Solution()
print so.removeNthFromEnd(a,1)