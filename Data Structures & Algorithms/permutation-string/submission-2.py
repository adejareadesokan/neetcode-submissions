class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l,r =0, len(s1)
        s = sorted(s1)
        while r < len(s2)+1:
            if  s == sorted(s2[l:r]):
                return True
            else:
                l += 1
                r += 1
        return False

