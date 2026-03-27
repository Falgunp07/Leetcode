class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        chars = []
        for char in paragraph:
            if char.isalnum():
                chars.append(char.lower())

            else:
                chars.append(" ")

        clean = "".join(chars)
        words = clean.split()

        banned_set = set(banned)
        counts = {}
        for word in words:
            if word not in banned_set:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
        return max(counts, key=counts.get)