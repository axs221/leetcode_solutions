# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return root.val
        return max(self.maxPathForNode(root))

    def maxCombo(self, left, val, right):
        maxCombo = val

        if left is not None:
            maxCombo = max(left, val, left + val)

        if right is not None:
            maxCombo = max(maxCombo, right, val, right + val)

        if left is not None and right is not None:
            maxCombo = max(maxCombo, left + right + val)

        # print 'max: %s, %s, %s = %s' % (left, val, right, maxCombo)

        return maxCombo

    def maxSinglePath(self, left, val, right):
        maxSinglePath = val

        if left is not None:
            maxSinglePath = max(left + val, maxSinglePath)

        if right is not None:
            maxSinglePath = max(right + val, maxSinglePath)

        return maxSinglePath

    def maxPathForNode(self, node):
        if node is None:
            return (None, None)

        leftMaxChild, left = self.maxPathForNode(node.left)
        val = node.val
        rightMaxChild, right = self.maxPathForNode(node.right)

        # onePathSum = max((left or 0), (right or 0)) + val
        onePathSum = self.maxSinglePath(left, val, right)
        comboChildren = self.maxCombo(left, val, right)
        maxChild = max(leftMaxChild, rightMaxChild, comboChildren)

        # print 'Val: %s (%s %s)' % (val, node.left and node.left.val, node.right and node.right.val)
        # print '===================='
        # print 'One: %s, %s, %s = %s' % (left, val, right, onePathSum)
        # print 'All: max(%s, %s, %s) = %s' % (leftMaxChild, rightMaxChild, comboChildren, maxChild)
        # print 'All: %s, One: %s' % (maxChild, onePathSum)
        # print

        return (maxChild, onePathSum)
