# or n = min(strings), O(n) solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # empty string if no prefix found
        res = ""
        # go through each letter of the first word in array
        for i in range(len(strs[0])):
            for ch in strs:
                # check if the first character is the same
                if i == len(ch) or ch[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        # no prefixes found
        return res