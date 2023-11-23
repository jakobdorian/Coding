# O(m * n) sol
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap mapping the char count to list of anagrams
        res = defaultdict(list)
        # go through list of strings
        for s in strs:
            # alphabet
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            # add this string to these particular anagrams
            res[tuple(count)].append(s)
        # only return values not keys
        return res.values()
