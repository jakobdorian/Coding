class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1, -1], float("inf")
        left = 0
        # edge cases
        if t == "":
            return ""
        countT, win = {}, {}
        # count of t
        for count in t:
            countT[count] = 1 + countT.get(count, 0)
        
        have, need = 0, len(countT)

        for right in range(len(s)):
            count = s[right]
            win[count] = 1 + win.get(count, 0)

            # does window meet cond?
            if count in countT and win[count] == countT[count]:
                have += 1

            while have == need:
                # update res
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                # pop from left of window
                win[s[left]] -= 1
                # update have count
                if s[left] in countT and win[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res

        if resLen != float("inf"):
            return s[left:right + 1]
        else:
            return ""
            