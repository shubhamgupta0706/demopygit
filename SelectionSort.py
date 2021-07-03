# Selection Sort
def sort(nums):
    for i in range(len(nums)):
        min = nums[i]
        pos = i
        for j in range(i, len(nums)):
            if nums[j] < min:
                min = nums[j]
                pos = j
        nums[i], nums[pos] = nums[pos], nums[i]


nums = [5, 3, 8, 2, 7, 34, 4, 1, 24]
sort(nums)

print(nums)