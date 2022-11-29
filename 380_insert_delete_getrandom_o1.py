import random
from collections import defaultdict
class RandomizedSet:
    """
    new record:
    runtime: 377ms, faster than 99.45%
    memory: 61.6mb, less than 22.58%
    
    old record:
    runtime 2032ms, faster than 5.11%
    memory: 61.5mb, less than 22.58%
    """

    def __init__(self):
        self.map = defaultdict(int)
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.values.append(val)
        self.map[val] = len(self.values) - 1
        
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.map:
            # swap val to be removed with last val
            # pop the last value
            # avoid shifting the entire array
            last_val = self.values[-1]
            idx_of_curr_val = self.map[val]
            
            # swap
            self.values[idx_of_curr_val] = last_val
            self.map[last_val] = idx_of_curr_val
            
            # set the last val to be the val to be removed
            self.values[-1] = val
            self.values.pop() # remove
            
            # remove from map
            self.map.pop(val)
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()