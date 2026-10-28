nums = [1000000000,-1000000000] 

def longestConsecutive(nums):
    unique_nums = set(nums)
    sorted_nums = sorted(unique_nums)
    seen = []
    list_of_lengths = []
    for x in sorted_nums:
        if seen:
            if x == seen[-1] + 1:
                seen.append(x)
                length_added_to_list = False
                continue
            else:
                list_of_lengths.append(len(seen))
                seen = []
                seen.append(x)
                length_added_to_list = True   
        else:
            seen.append(x)
    if not length_added_to_list:
        list_of_lengths.append(len(seen))

    return max(list_of_lengths)



if __name__ == "__main__":
    print(longestConsecutive(nums))