numbers = [1,2,3,4]
target = 3

def twoSum(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while True:
        if numbers[left_pointer] + numbers[right_pointer] > target:
            right_pointer-=1
        elif numbers[left_pointer] + numbers[right_pointer] < target:
            left_pointer+=1
        else:
            return [left_pointer+1, right_pointer+1]


if __name__ == "__main__":

    print(twoSum(numbers, target))
