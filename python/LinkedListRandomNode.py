'''
    reservoir sampling
    概率问题，比如有n个数，第n个数的概率为1/n, 选second-to-last的数1/(n-1) * (1 - 1/n) = 1/n
    也就是说,没选第n个数(1-1/n)，选了第n-1个数(1/(n-1))
    以此类推，选一个数的概率 1* 1/2 * 2/3 *...*n-1/n = 1/n
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head
        ans = cnt = 0
        while node:
            #The probablity that ith element is replaced is 1/i
            #reservoir sampling
            #https://gregable.com/2007/10/reservoir-sampling.html
            if random.randint( 0, cnt ) == 0:
                ans = node.val
            node, cnt = node.next, cnt+1
        return ans
