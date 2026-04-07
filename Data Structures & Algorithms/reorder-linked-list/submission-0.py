# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findMid(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(h):
            prev = None
            while h:
                nxt = h.next
                h.next = prev
                prev = h
                h = nxt
            return prev

        mid = findMid(head)
        nxt = mid.next
        mid.next = None
        tmp = reverse(nxt)
        dummy = ListNode()
        curr = dummy
        check = True
        while head and tmp:
            if check:
                curr.next =head
                head = head.next
            else:
                curr.next = tmp
                tmp = tmp.next
            curr = curr.next
            check = not check
        if head:
            curr.next = head
        else:
            curr.next = tmp
        # return dummy.next
