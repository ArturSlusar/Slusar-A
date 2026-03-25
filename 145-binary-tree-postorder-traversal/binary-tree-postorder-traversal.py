# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node):
            #Если узла нет то выходим из рекурсии
            if not node:
                return

            #Рекурсивно смотрим левое дерево
            dfs(node.left)        
            #Потом правое
            dfs(node.right)
            #Обрабатываем узел после посещения всез потомкоы
            res.append(node.val)

        dfs(root)

        return res
