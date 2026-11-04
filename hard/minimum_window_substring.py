s = "xyz"
t = "xyz"

def minWindow(s, t):

    countT, window = {}, {}

    for character in t:
        countT[character] = 1 + countT.get(character, 0)

    need, have = len(countT),  0
    left_pointer = 0
    substring = [-1, -1]
    substring_length = float('inf')

    for right_pointer in range(len(s)):
        window[s[right_pointer]] = 1 + window.get(s[right_pointer], 0)

        if s[right_pointer] in countT and window[s[right_pointer]] == countT[s[right_pointer]]:
            have += 1

        while have == need:
            if (right_pointer - left_pointer + 1) < substring_length:
                substring = [left_pointer, right_pointer]
                substring_length = right_pointer - left_pointer + 1
            window[s[left_pointer]] -= 1

            if s[left_pointer] in countT and window[s[left_pointer]] < countT[s[left_pointer]]:
                have-=1
            left_pointer += 1

    return s[substring[0]: substring[1]+1] if substring_length != float('inf') else ""

if __name__ == "__main__":

    print(minWindow(s,t))
                    