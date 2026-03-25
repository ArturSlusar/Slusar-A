# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Список для хранения итогового результата обхода
        result = []
        
        def traverse(node):
            # Базовый случай: если узел пуст, возвращаемся назад
            if not node:
                return
            
            # 1. Сначала идем в крайнюю левую точку (рекурсивный шаг)
            traverse(node.left)
            
            # 2. Добавляем значение текущего узла в список
            # Это происходит, когда всё левое поддерево уже обработано
            result.append(node.val)
            
            # 3. Переходим к обработке правого поддерева
            traverse(node.right)
            
        # Запускаем рекурсию от корня дерева
        traverse(root)
        
        return result
        