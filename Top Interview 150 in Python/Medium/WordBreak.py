class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # initialize a dynamic programming list
        dp = [False] * (len(s) + 1)
        # set the last element of dp to True, as an empty string is always valid
        dp[len(s)] = True

        # iterate through the string 's' backwards
        # complexity: O(n*m), where n is the length of string 's' and m is the average length of words in wordDict
        for i in range(len(s) - 1, -1, -1):
            # check each word in wordDict
            for word in wordDict:
                # check if the current substring matches the word in wordDict
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    # update dp[i] to True if the substring matches and dp[i + len(word)] is also True
                    dp[i] = dp[i + len(word)]
                # if dp[i] is already True, break out of the loop
                if dp[i]:
                    break
        # return dp[0], which indicates whether the entire string can be segmented using the words in wordDict
        return dp[0]
