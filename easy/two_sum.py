
nums = [5,5]
target = 10

def twoSum(nums, target):
    seen = {}

    for index, number in enumerate(nums):
        if target - number in seen:
            return [seen[target - number], index]
        else:
            seen[number] = index


if __name__ == '__main__':

    print(twoSum(nums, target))

