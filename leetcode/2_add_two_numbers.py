# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ret = ListNode(0)
        carry = 0
        while True:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            add = val1 + val2 + carry
            carry = add // 10
            ans.val = add % 10
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
               
            if l1 is None and l2 is None:
                break
            
            ans.next = ListNode(0)
            ans = ans.next
            
        if carry > 0:
            ans.next = ListNode(carry)
        return ret
        
        
            
            
        