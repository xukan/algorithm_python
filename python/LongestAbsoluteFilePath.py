'''
Created on Aug 24, 2016

@author: Onerepublic
'''
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res = 0
        stack = [ ( -1 , 0 )]
        for p in input.splitlines():
            depth = p.count( '\t' )
            name = p.replace( '\t', '' )
            topDepth, topLength = stack[-1]
            while( depth <= topDepth ):
                stack.pop()
                topDepth, topLength = stack[-1]
            length = len( name ) + ( depth > 0 )
            stack.append(( depth, length+topLength ))
            if name.count('.'):
                res = max( res, length+topLength ) 
        return res
    
if __name__ == '__main__':
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    result = Solution().lengthLongestPath(input)
    print result