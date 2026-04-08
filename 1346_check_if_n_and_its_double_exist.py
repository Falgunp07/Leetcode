class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arr.sort()
        n = len(arr)
        for i in range(n):
            target = 2 * arr[i]
            low = 0
            high = n - 1
            
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == target and mid != i:
                    return True
                
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return False