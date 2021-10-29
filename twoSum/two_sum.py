def solve(nums, target): 
     s=set()
     arr=[0,0]
     for elem in nums:
         s.add(elem)
     for i in range(len(nums)):
         if target-nums[i] in s:
             arr[0]=i
     for j in range(len(nums)):
         if nums[j]==target-nums[arr[0]] and j!=arr[0]:
             arr[1]=j
     return arr

nums=[3,2,4]
target=6
print(solve(nums,target))
