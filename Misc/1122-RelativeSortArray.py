class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # set for O(1) lookups
        arr2_set = set(arr2)
        
        # dictionary to count occurrences of each number in arr1
        arr1_count = defaultdict(int)
        
        # list to store elements that are in arr1 but not in arr2
        end = []
        
        # iterate through each number in arr1
        for n in arr1:
            # if the number is not in arr2, add it to the 'end' list
            if n not in arr2_set:
                end.append(n)
            # increment the count for the number in arr1_count dictionary
            arr1_count[n] += 1
        
        # sort the 'end' list as it should appear in ascending order at the end of the result
        end.sort()

        # result list to store the final sorted array
        res = []
        
        # iterate through each number in arr2
        for n in arr2:
            # append the number to the result list as many times as it appears in arr1
            for _ in range(arr1_count[n]):
                res.append(n)

        # combine the sorted 'res' list with the sorted 'end' list
        return res + end
        