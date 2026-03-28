
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(area ** 0.5)
        
        while W > 0:
            if area % W == 0:
                L = area // W
                return [L, W]
            W -= 1