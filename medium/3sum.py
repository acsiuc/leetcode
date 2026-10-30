numbers = [0,0,0]

def threeSum(numbers):
    numbers.sort()
    triplets = []

    for index, number in enumerate(numbers):
        if index > 0 and number == numbers[index-1]:
            continue

        left_pointer, right_pointer = index + 1, len(numbers)-1

        while left_pointer < right_pointer:
            threeSum = number + numbers[left_pointer] + numbers[right_pointer]

            if threeSum > 0:
                right_pointer-=1
            elif threeSum < 0:
                left_pointer +=1
            else:
                triplets.append([number,numbers[left_pointer], numbers[right_pointer]])
                left_pointer +=1
                while numbers[left_pointer] == numbers[left_pointer - 1] and left_pointer < right_pointer:
                    left_pointer +=1

    return triplets


if __name__ == "__main__":
    print(threeSum(numbers))