# O(1) time complexity
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            i = self.numMap[val]
            last_val = self.numList[-1]
            self.numList[i] = last_val
            self.numList.pop()
            self.numMap[last_val] = i
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()