class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            wset = set(word.lower())


            if wset <= row1 or wset <= row2 or wset <= row3:
                result.append(word)

        return result