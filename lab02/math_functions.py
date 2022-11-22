def average(nums):
    if not isinstance(nums, list):
        return
    return sum_of_vals(nums) / len(nums)

def max_val(nums):
    if not isinstance(nums, list):
        return
    maximum = nums[0]
    for x in range(1, len(nums)):
        if nums[x] > maximum:
            maximum = nums[x]
    return max

def min_val(nums):
    if not isinstance(nums, list):
        return
    minimum = nums[0]
    for x in range(1, len(nums)):
        if nums[x] < minimum:
            minimum = nums[x]
    return min

def sum_of_vals(nums):
    if not isinstance(nums, list):
        return
    s = 0
    for n in nums:
        s += n
    return s

if __name__ == "__main__":
    nums_list = list()
    nums_list.append(1)
    nums_list.append(2)
    nums_list.append(3)
    nums_list.append(4)
    nums_list.append(5)
    print(nums_list)

    print("Sum:", sum_of_vals(nums_list))
    print("Average:",average(nums_list))
    print("Highest:", max_val(nums_list))
    print("Lowest:", min_val(nums_list))
