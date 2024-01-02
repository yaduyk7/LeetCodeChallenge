import random
class RandomizedSet(object):

    def __init__(self):
        self.new_set=set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.new_set:
            self.new_set.add(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.new_set:
            self.new_set.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.new_set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()