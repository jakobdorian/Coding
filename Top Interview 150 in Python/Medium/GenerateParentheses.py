class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # helper function to generate valid parentheses combinations recursively
        # left: number of remaining left parentheses
        # right: number of remaining right parentheses
        # stack: current balance of open parentheses
        # cand: current combination being built
        def helper(left, right, stack, cand):
            # base case: If there are no more left and right parentheses, add the combination to the result
            if left == right == 0:
                res.append(cand)
            # recursive cases:
            # if there are remaining left parentheses, add "(" and recurse
            if left > 0:
                helper(left - 1, right, stack + 1, cand + "(")
            # if there are remaining right parentheses and the current balance allows, add ")" and recurse
            if right > 0 and stack > 0:
                helper(left, right - 1, stack - 1, cand + ")")
        # start the recursive process with initial parameters
        helper(n, n, 0, "")
        # return the list of valid parentheses combinations
        return res
