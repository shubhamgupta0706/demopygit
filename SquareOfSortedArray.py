class Solution:

    def __init__(self):
        pass

    def sortedSquares(self, nums, n):
        for i in range(n):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums


items = input()
items = items.replace("[", "")
items = items.replace("]", "")
my_list = items.split(",")

for i in range(0, len(my_list)):
    my_list[i] = int(my_list[i])

sol = Solution()
resulted_list = sol.sortedSquares(my_list, len(my_list))

print('[', end='')
for i in range(0, len(resulted_list)):
    print(resulted_list[i], end='')
    if i == len(resulted_list)-1:
        print(end='')
    else:
        print(end=',')
print(']', end='')