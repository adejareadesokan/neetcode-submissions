class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decA = int(a,2)
        decB = int(b,2)
        return bin((decA + decB))[2:]
        