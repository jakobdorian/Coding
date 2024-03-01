class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # lengths of input strings
        len1, len2 = len(str1), len(str2)

        # helper function to check if the current length `l` is a divisor of both lengths
        def helper(l):
            if len1 % l or len2 % l:
                return False
            # calculate how many times the substrings repeat in the strings
            f1, f2 = len1 // l, len2 // l
            # check if substrings constructed using the first `l` characters can generate both strings
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # iterate over possible lengths of greatest common divisors, starting from the minimum length
        for l in range(min(len1, len2), 0, -1):
            # if the current length `l` is a common divisor, return the substring of `str1` of length `l`
            if helper(l):
                return str1[:l]
        # if no common divisor is found, return an empty string
        return ""

