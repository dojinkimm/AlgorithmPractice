# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return ListNode("")
        
        ans = ret = ListNode(0)
        nums = []
        while True:
            if l1 is not None and l2 is not None:
                nums.extend([l1.val, l2.val])
            elif l1 is not None:
                nums.append(l1.val)
            elif l2 is not None:
                nums.append(l2.val)
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
            if l1 is None and l2 is None:
                break
                
        length = len(nums)
        for i, n in enumerate(sorted(nums)):
            ans.val = n
            if i < length-1:
                ans.next = ListNode(0)
                ans = ans.next
            
        return ret