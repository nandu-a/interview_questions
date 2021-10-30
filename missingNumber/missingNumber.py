# Time complexity - O(n)
# Space complexity - O(1)
def missingNumber(nums) -> int:
    length = len(nums)
        
    return ((length * (length + 1)) // 2) - sum(nums)

print(missingNumber([9,6,4,2,3,5,7,0,1]))

