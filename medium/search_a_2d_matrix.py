matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15


def searchMatrix(matrix, target):
    left = 0
    right = len(matrix) - 1

    while left <= right:
        mid = (left+right) // 2

        if matrix[mid][-1] < target:
            right = mid -1
        elif matrix[mid][0] > target:
            left = mid + 1
        else:
            break

    if left > right:
        return False

    left = 0
    right = len(matrix) - 1
    matricea = matrix[mid]

    while left <= right:
        mid = (left+right) // 2

        if matricea[mid] > target:
            right = mid -1
        elif matricea[mid] < target:
            left = mid + 1
        else:
            return True

    return False


if __name__ == "__main__":
    print(searchMatrix(matrix, target))