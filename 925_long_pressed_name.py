class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        n, m = len(name), len(typed)
        
        for j in range(m):
            if i < n and name[i] == typed[j]:
                i += 1
            elif j > 0 and typed[j] == typed[j-1]:
                continue
            else:
                return False
        return i == n