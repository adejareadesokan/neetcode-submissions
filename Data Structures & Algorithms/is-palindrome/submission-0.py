class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str +=char.lower()
        left = 0
        right = len(new_str) -1
        while right >= left:
            if new_str[right] != new_str[left]:
                return False
            left += 1
            right -= 1
        return True
        

        