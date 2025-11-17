# تعريف عقدة الشجرة الثنائية
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        دالة تتحقق إذا كانت الشجرة الثنائية متوازنة
        """
        def check(node):
            # قاعدة النهاية: إذا كانت الشجرة فارغة
            if not node:
                return 0, True  # عمق 0، متوازنة True
            
            left_depth, left_balanced = check(node.left)
            right_depth, right_balanced = check(node.right)
            
            # الفرق بين العمق الأيسر والأيمن
            if abs(left_depth - right_depth) > 1:
                return 0, False
            
            # العمق الحالي
            depth = 1 + max(left_depth, right_depth)
            
            # الشجرة متوازنة إذا كان كل فرع متوازن
            return depth, left_balanced and right_balanced
        
        # نرجع فقط True أو False
        return check(root)[1]

# مثال للتجربة
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    sol = Solution()
    print(sol.isBalanced(root))  # True
