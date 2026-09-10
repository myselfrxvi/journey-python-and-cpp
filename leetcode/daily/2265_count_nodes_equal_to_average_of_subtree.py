class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def postorder(node):
            if not node:
                return 0, 0 
            l_sum, l_count = postorder(node.left)
            r_sum, r_count = postorder(node.right)
            current_sum = node.val + l_sum + r_sum
            current_count = 1 + l_count + r_count
            if current_sum // current_count == node.val:
                self.ans += 1
            return current_sum, current_count
        postorder(root)
        return self.ans