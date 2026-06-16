def count_pairs(nums, k):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count

# Example
print(count_pairs([3,1,2,2,2,1,3], 2))  # 4
print(count_pairs([1,2,3,4], 1))        # 0