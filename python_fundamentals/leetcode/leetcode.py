from typing import TypeVarTuple
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_rev = dummy

        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = get_kth(group_rev, k)
            if not kth:
                break 
            group_next = kth.next
            first = group_rev.next
            prev = group_next
            curr = first
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev=curr
                curr = nxt
            group_rev.next = kth 
            group_rev = first
            
        return dummy.next
            