# BubbleSort
def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


nums = [5, 3, 8, 2, 7, 9, 4]
sort(nums)

print(nums)