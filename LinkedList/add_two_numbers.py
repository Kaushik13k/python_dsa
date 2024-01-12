# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        dummy_node = ListNode(-1)
        current = dummy_node
        carry = 0

        while t1 is not None or t2 is not None:
            _sum = carry

            if t1:
                _sum += t1.val
                t1 = t1.next

            if t2:
                _sum += t2.val
                t2 = t2.next
            digit = int(_sum%10)
            carry = int(_sum/10)
            new_node = ListNode(digit)
            current.next = new_node
            current = current.next

        if carry:
            current.next = ListNode(carry)
        return dummy_node.next