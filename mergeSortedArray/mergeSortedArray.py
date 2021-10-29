

def merge(nums1, m: int, nums2, n: int) -> None:
    pointer1 = m - 1
    pointer2 = n - 1
    
    index = len(nums1) - 1
        
    while pointer1 > -1 and pointer2 > -1 and index > -1:
        if nums1[pointer1] > nums2[pointer2]:
            nums1[index] = nums1[pointer1]
            pointer1 -= 1
        else:
            nums1[index] = nums2[pointer2]
            pointer2 -= 1
                
        index -= 1

    while pointer2 > -1:
        nums1[index] = nums2[pointer2]
        pointer2 -= 1
        index -= 1

nums1 = [1, 4, 6, 0, 0, 0]
nums2 = [2, 3, 5]

merge(nums1, 3, nums2, 3)

print(nums1)
