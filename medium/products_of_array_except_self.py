
nums = [-1,0,1,2,3]


def productExceptSelf(nums):
    prefixes = [1]
    suffixes = [1]
    answer = []
    for x in nums:
        if len(prefixes) < len(nums):
            prefixes.append(prefixes[-1]*x)
        
    for x in nums[::-1]:
        if len(suffixes) < len(nums):
            suffixes.append(suffixes[-1]*x)

    suffixes.reverse()
    for y in range(len(nums)):
        answer.append(prefixes[y]*suffixes[y])

    return answer

if __name__ == "__main__":
    print(productExceptSelf(nums))