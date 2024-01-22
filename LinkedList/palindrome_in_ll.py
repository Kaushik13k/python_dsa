# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        first = head
        second = None

        # Find the mid of LL
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the 2nd half Of LL
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the elements
        second = prev
        while second:
            if first.val != second.val:
                return False
            second = second.next
            first = first.next

        return True
