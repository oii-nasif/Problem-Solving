from unittest import result


def generate_subarray(nums):
    n = len(nums)

    # max_sum = -1000000

    # for l in range(1, n+1):   # O(n)
    #     for i in range(n-l+1):  # O(n)
    #         sum_ = sum(nums[i:i+l])  # O(n)
    #         if sum_ > max_sum:
    #             max_sum = sum_

    # return max_sum
    # Time Complexity: O(n*n*n) = O(n^3)
    # Space Complexity: O(1)


    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, n):
        if nums[i] + current_sum > nums[i]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

    # Time Complexity: O(n)
    # Space Complexity: O(1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(generate_subarray(nums))