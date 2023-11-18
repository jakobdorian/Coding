# n log n + m log m sol
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # edge cases
        if len(ransomNote) > len(magazine):
            return False
        
        ran = sorted(list(ransomNote))
        mag = sorted(list(magazine))

        for ch in mag:
            # check if the first character of mag is the same as ransom
            if ran and ch == ran[0]:
                ran.pop(0)
            # check if ransom still exists
        if ran:
            return False
        else:
            return True
