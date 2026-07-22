class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        srt = sorted(nums)
        n = len(srt)

        for i in range(n - 2):
            if i > 0 and srt[i] == srt[i - 1]:
                continue  

            target = -srt[i]
            j, k = i + 1, n - 1

            while j < k:
                total = srt[j] + srt[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    result.append([srt[i], srt[j], srt[k]])
                    j += 1
                    k -= 1
                    while j < k and srt[j] == srt[j - 1]:
                        j += 1  
                    while j < k and srt[k] == srt[k + 1]:
                        k -= 1  

        return result

        