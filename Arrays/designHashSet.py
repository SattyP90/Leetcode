class MyHashSet(object):

    def __init__(self):
        self.hashSet = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """

        
        noRep = True
        for n in self.hashSet:
            if n == key:
                noRep = False
                break
            
        if noRep:
            self.hashSet.append(key)
            
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """


        for n in self.hashSet:
            if n == key:
                self.hashSet.remove(key)


    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """

        for n in self.hashSet:
            if n == key:
                return True
        
        return False


# class MyHashSet(object):

#     def __init__(self):
#         self.hashSet = []

#     def add(self, key):
#         if key not in self.hashSet:
#             self.hashSet.append(key)

#     def remove(self, key):
#         if key in self.hashSet:
#             self.hashSet.remove(key)

#     def contains(self, key):
#         return key in self.hashSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)