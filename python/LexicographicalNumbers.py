'''
Created on Aug 24, 2016

@author: Onerepublic
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #可以类比二叉树先根遍历的迭代算法，需要用到栈（Stack）数据结构
        result = []
        stack = [1]
        while stack:
            y = stack.pop()
            result.append(y)
            if y < n and y % 10 < 9:
                stack.append( y + 1 )
            if y * 10 <= n: 
                stack.append( y * 10 )
        return result
            
if __name__ == '__main__':
    input = 23
    result = Solution().lexicalOrder( input )
    print result
        