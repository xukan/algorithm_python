'''
[ 1, 2, 3 ]
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Backtracking
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = []
        result = []
        if not nums:
            return result
        self.helper( nums, stack, result )
        return result
            
    def helper(self, nums, stack, result):
        if len( stack ) == len( nums ):
            result.append( []+stack )
            return
        
        for index, item in enumerate( nums ):
            if item not in stack:
                stack.append( item )
                self.helper(nums, stack, result)
                stack.pop()
            
if __name__ == '__main__':
    input = [ 1, 2, 3 ]
    result = Solution().permute( input )
    print result