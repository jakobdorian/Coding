class Solution:
    def intToRoman(self, num: int) -> str:
        # list of roman map to int
        roman = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9],
        ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
        ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

        res = ''
        for sym, val in reversed(roman):
            if num // val:
                # add sym to res
                count = num // val
                res += (sym * count)
                # update value
                num = num % val
        return res
        