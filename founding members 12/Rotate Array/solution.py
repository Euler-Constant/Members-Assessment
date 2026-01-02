def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    n = len(nums)
    k = k % n
    
    reverse(0, n - 1)
    reverse(0, k)
    reverse(k + 1, n - 1)