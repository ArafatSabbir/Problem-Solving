# Runtime: 56 ms, faster than 29.99% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 14.2 MB, less than 45.49% of Python3 online submissions for Find Numbers with Even Number of Digits.



class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i))%2 == 0:
                count += 1 
        return count
    
    

# Runtime: 44 ms, faster than 96.07% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 14.5 MB, less than 17.82% of Python3 online submissions for Find Numbers with Even Number of Digits.
    
    
    
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(i)) % 2 == 0 for i in nums)
