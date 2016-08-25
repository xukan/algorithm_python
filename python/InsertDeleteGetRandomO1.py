'''
数组存储元素， hashtable维护元素在数组的下标
利用hashtable, hashtable的新增/删除操作是O(1), 数组的随机访问也是O(1)
'''

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            return False
        self.data.append( val )
        self.index[ val ] = len( self.data ) -1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            return False
        idx = self.index[ val ]
        tmp = self.data[ -1 ]
        self.data[ idx ] = tmp
        self.index[ tmp ] = idx
        self.data.pop()
        del self.index[ val ]
        return True
            

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data)
        #size = len( self.data )
        #index = random.randint( 0, size-1 )
        #return self.data[ index ]