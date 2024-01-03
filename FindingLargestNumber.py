"""
Find the Largest Number in a List
-solved by Adnan
"""


def find_largest_nums(nums):
    # check if the list is empty or not
    if not nums:
        return None

        # initialize the largest number with the first element
    largest = nums[0]

    for num in nums:
        print(num)
        if num > largest:
            largest = num

            # Return the largest number
    return largest


# test case

arr = [1, 2, 3, 4, 5]
print("The largest number is : ", find_largest_nums(arr))
