class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr = []
        curr_len = 0 
        i = 0

        while i < len(words):
            if curr_len + len(curr) + len(words[i]) > maxWidth:
                extra = maxWidth - curr_len
                spaces = extra // max(1, len(curr) - 1)
                # mod it
                remainder = extra % max(1, len(curr) - 1)

                for j in range(max(1, len(curr) - 1)):
                    curr[j] += " " * spaces
                    # there is remainder
                    if remainder:
                        curr[j] += " "
                        remainder -= 1

                res.append("".join(curr))
                # reset line and length
                curr, curr_len = [], 0
                continue
            
            # line is complete
            curr.append(words[i])
            curr_len += len(words[i])
            i += 1
        # handle last line
        last = " ".join(curr)
        trail = maxWidth - len(last)
        res.append(last + " " * trail)
        return res
        