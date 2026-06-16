def find_intersection_values(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = sum(1 for x in nums1 if x in set2)
    answer2 = sum(1 for x in nums2 if x in set1)

    return [answer1, answer2]

# Example
print(find_intersection_values([2,3,2], [1,2]))      # [2,1]
print(find_intersection_values([4,3,2,3,1], [2,2,5,2,3,6]))  # [3,4]