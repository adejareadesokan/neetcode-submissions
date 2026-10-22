class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def bitsperiter(num):
            res2 = 0
            while num:
                num = (num & (num -1))
                res2 += 1
            return res2
        for i in range(n+1):
            res.append(bitsperiter(i))
        return res

            
        