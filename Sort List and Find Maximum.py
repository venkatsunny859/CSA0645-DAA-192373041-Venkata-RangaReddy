def sort_and_find_max(lst):
    if not lst:
        return None

    lst.sort()
    return lst[-1]

print(sort_and_find_max([]))                 # None
print(sort_and_find_max([5]))                # 5
print(sort_and_find_max([3,3,3,3,3]))        # 3