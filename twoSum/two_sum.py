

# Time Complexity - O(n)
# Space Complexity - O(n)

def solve(nums, target): 
     s=set()
     arr=[0,0]
     for elem in nums:
         s.add(elem)  # all the elements in nums are added into a hash map
     for i in range(len(nums)):
         if target - nums[i] in s:
             arr[0] = i
     for j in range(len(nums)):
         if nums[j] == target-nums[arr[0]] and j!=arr[0]:
             arr[1]=j
     return arr  #  an array is returned

nums = [3,2,4]  # sample input
target = 6
print(solve(nums, target))
