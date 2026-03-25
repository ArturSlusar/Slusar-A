# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lo=-float('inf'), hi=float('inf')) -> bool:
        # Если узла нет — это не ошибка, возвращаем True
        if not root:
            return True
        
        # Если текущее число вышло за рамки (меньше минимума или больше максимума)
        if not (lo < root.val < hi):
            return False
        
        # Рекурсивно проверяем лево (меняем максимум) и право (меняем минимум)
        # Если хотя бы одна сторона вернет False, вся функция вернет False
        return self.isValidBST(root.left, lo, root.val) and \
               self.isValidBST(root.right, root.val, hi)
        