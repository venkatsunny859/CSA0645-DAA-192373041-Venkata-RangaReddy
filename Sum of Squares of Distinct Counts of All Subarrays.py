def sum_counts(nums):
    ans = 0

    for i in range(len(nums)):
        distinct = set()

        for j in range(i, len(nums)):
            distinct.add(nums[j])
            ans += len(distinct) ** 2

    return ans

# Example
print(sum_counts([1,2,1]))  # 15
print(sum_counts([1,1]))    # 3