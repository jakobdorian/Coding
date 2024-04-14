from sortedcontainers import SortedSet

class SmallestInfiniteSet:
    def __init__(self):
        self.sorted_list = SortedSet()
        # adding integers from 1 to 1004 (inclusive) to the sorted list
        for i in range(1, 1005):
            self.sorted_list.add(i)
    # removes and returns the smallest element from the set.
    def popSmallest(self) -> int:
        # getting the smallest element
        x = self.sorted_list[0]
        self.sorted_list.remove(x)
        return x
        
    def addBack(self, num: int) -> None:
        # adding the number to the set
        self.sorted_list.add(num)
        