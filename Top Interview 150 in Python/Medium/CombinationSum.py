class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # store combinations for each value from 0 to 'target'
        res = [[] for _ in range(target+1)]
        for c in candidates:
            # iterate through each value from 1 to 'target'
            for i in range(1, target+1):
                # if the current value is less than the candidate, skip
                if i < c: 
                    continue
                # if the current value is equal to the candidate, add a combination with only the candidate
                if i == c:
                    res[i].append([c])
                else:
                    # for values greater than the candidate, add combinations using previously calculated results
                    for b in res[i-c]:
                        res[i].append(b+[c])
        # return the combinations for the target value
        return res[target]
