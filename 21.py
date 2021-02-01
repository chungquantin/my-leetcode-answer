# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
ln1 = ListNode(val=1, next=ListNode(val=2,next=ListNode(4)))
ln2 = ListNode(val=1, next=ListNode(val=3,next=ListNode(4)))

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cur = res
        while (l1 and l2):
            if (l1.val > l2.val):
                cur.next = l2
                l2 = l2.next
            else: 
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if (l1): 
            cur.next = l1 
        else: 
            cur.next = l2
        res = res.next
        return res
            
    
    
print("Result: ",Solution().mergeTwoLists(ln1,ln2))