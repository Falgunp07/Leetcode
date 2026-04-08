class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return letters[low % n]