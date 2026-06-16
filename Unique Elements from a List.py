def unique_elements(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(unique_elements([3,7,3,5,2,5,9,2]))
# [3,7,5,2,9]

print(unique_elements([-1,2,-1,3,2,-2]))
# [-1,2,3,-2]