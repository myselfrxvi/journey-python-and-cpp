# LeetCode 25: Reverse Nodes in k-Group (Hard)
# Pattern: In-Place Pointer Rewiring / Group Traversal
# Time Complexity: O(N), Space Complexity: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

            # Reverse group
            prev = group_next
            curr = first
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect
            group_rev.next = kth
            group_rev = first

        return dummy.next

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    print("Reversed in k=2:", to_list(s.reverseKGroup(head, 2)))
