def singleNumber(nums):
    """
    Returns the single number that appears once in the array.

    :param nums: A non-empty list of integers.
    :return: The single number that appears once.
    """
    result = 0
    for num in nums:
        result ^= num
    return result
num=[4,1,2,1,2]
print(singleNumber(num))