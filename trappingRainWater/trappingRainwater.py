"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
# input - list
# output - integer
# Time complexity - O(n)
# Space complexity - O(1)
def trappingRainWater(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1

    return water

height = int(input());
trappingRainWater(height)
