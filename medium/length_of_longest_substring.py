
string = 'bacad'

def lengthOfLongestSubstring(string):
    seen = set()
    left_pointer = 0
    longest_substring = 0

    for right_pointer in range(len(string)):
        while string[right_pointer] in seen:
            seen.remove(string[left_pointer])
            left_pointer+=1
        seen.add(string[right_pointer])
        longest_substring = max(longest_substring, len(seen))

    return longest_substring

if __name__ == "__main__":
    print(lengthOfLongestSubstring(string))