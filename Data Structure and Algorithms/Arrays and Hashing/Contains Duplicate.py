class Solution:
    def containsDuplicate(self, nums):
        s=set()
        for num in nums:
            if(num in s):
                return True
            s.add(num)
        return False

sol=Solution()
print(sol.containsDuplicate([1,2,3,1]))

