# Given a roman numeral, convert it to an integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        # a hashmap for all the roman numerals
        roman_nums = {"I" : 1, "V": 5, "X" : 10,
        "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_nums[s[i]] < roman_nums[s[i+1]]:
                res -= roman_nums[s[i]]
            else:
                res += roman_nums[s[i]]
        return res