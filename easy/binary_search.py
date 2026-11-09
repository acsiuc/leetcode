import copy

nums = [4]
target = 4


def search(nums, target):

    left = 0
    right = len(nums) - 1

    while nums and left <= right:
        mid  = (left + right) // 2
        print(nums[mid])
        if nums[mid] > target:
            right = mid -1  
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    print(search(nums, target))