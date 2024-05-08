class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result list with zeros, same length as input temperatures
        res = [0] * len(temperatures)
        stack = []

        # iterate through the temperatures list with index
        for i, t in enumerate(temperatures):
            # while stack is not empty and current temperature is higher than the temperature at the top of stack
            while stack and t > stack[-1][0]:
                # pop the temperature and its index from stack
                temp, index = stack.pop()
                # update result at index to the difference between current index and popped index
                res[index] = (i - index)
            # append current temperature and its index to stack
            stack.append([t, i])
        
        # return the resulting list
        return res
