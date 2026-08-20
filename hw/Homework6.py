def two_sum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(f"nums = {nums}")
print(f"target = {target}")
print(f"Результат: {result}")

print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))