nums = [1,2,3,3]

def hasDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        elif x not in seen:
            seen.add(x)
    
    return False


if __name__ == '__main__':

    print(hasDuplicate(nums=nums))