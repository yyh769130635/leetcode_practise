# 通过层次遍历输出中序遍历
import math

# nums = [i for i in range(15)]
nums = [1, 2, 9, 5, -1, 7, 6]
n = len(nums)


def inorder(nums, i):
    if i >= n:
        return []
    if nums[i] == -1:
        return []
    left = inorder(nums, 2 * i + 1)
    right = inorder(nums, 2 * i + 2)
    return left + [nums[i]] + right


ans = inorder(nums, 0)
print(ans)
