s = "xyz"
t = "xyz"

def minWindow(s, t):

    if t == "": return ""

    countT, window = {}, {}

    for character in t:
        countT[character] = 1 + countT.get(character, 0)

    have, need = 0, len(countT)
    substring, substring_length = [1, -1], float("infinity")
    left_pointer = 0

    for right_pointer in range(len(s)):
        character = s[right_pointer]
        window[character] = 1 + window.get(character, 0)

        if character in countT and window[character] == countT[character]:
            have += 1

        while have == need:
            if (right_pointer - left_pointer + 1) < substring_length:
                substring = [left_pointer, right_pointer]
                substring_length = (right_pointer - left_pointer + 1)
            window[s[left_pointer]] -= 1
            if s[left_pointer] in countT and window[s[left_pointer]] < countT[s[left_pointer]]:
                have -= 1
            left_pointer += 1

    left_pointer, right_pointer = substring

    return s[left_pointer: right_pointer + 1] if substring_length != float("infinity") else ""

if __name__ == "__main__":

    print(minWindow(s,t))
                    