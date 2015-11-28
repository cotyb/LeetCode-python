# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        tmp1 = head
        tmp2 = head
        count = 1
        while tmp1.next:
            tmp1 = tmp1.next
            count += 1
        tmp1 = head
        left = right = count / 2
        curr_node = None
        while right:
            tmp1 = tmp1.next
            right -= 1
        while left:
            head = tmp2
            next_node = tmp2.next
            tmp2.next = curr_node
            curr_node = tmp2
            tmp2 = next_node
            left -= 1
        if count % 2 == 0:
            return self.compare(head,tmp1)
        else:
            return self.compare(head,tmp1.next)

    def compare(self,head,tmp):
        while head.next and tmp.next:
            if head.val != tmp.val:
                return False
            else:
                head = head.next
                tmp = tmp.next
        return head.val == tmp.val

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
so = Solution()
print so.isPalindrome(a)