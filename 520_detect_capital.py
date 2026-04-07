class Solution:
    def detectCapitalUse(self, word: str):
        caps = 0
        for char in word:
            if char.isupper():
                caps += 1
        
        n = len(word)
        if caps == n:
            return True
        if caps == 0:
            return True
        if caps == 1 and word[0].isupper():
            return True
        return False