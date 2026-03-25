# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node: #Если узел пуст возвращаемся обратно по стеку рекурсии
                return
            
            #Обрабатываем сам узел, сначала добавляем значения в результат до перехода к потомкам
            res.append(node.val)

            #Преходим в левую часть дерева
            dfs(node.left)

            #Переходим в правую часть дерева
            dfs(node.right)

        dfs(root)    #Запускаем обход от корня

        return res