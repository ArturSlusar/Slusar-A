# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Если доходим до пустого места то создаем новый узел
        if not root:
            return TreeNode(val)

        #Если число которое мы вставили меньше текущего то идем на лево
        if val < root. val:
            #Обнавляем левую ветку нашим числом
            root.left = self.insertIntoBST(root.left, val)
        else:
            #Если число больше то идем направо
            root.right = self.insertIntoBST(root.right, val)
        #Возвращаем текущий корень
        return root

        