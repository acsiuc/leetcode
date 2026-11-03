string = "XYYX"
k=2

def characterReplacement(string, k):
    left_pointer = 0
    counter = {}
    result = 0

    for right_pointer in range(len(string)):
        counter[string[right_pointer]] = 1 + counter.get(string[right_pointer], 0)

        while (right_pointer - left_pointer + 1) - max(counter.values()) > k:
            counter[string[left_pointer]] -= 1
            left_pointer += 1

        result = max(result, right_pointer - left_pointer + 1)

    return result


if __name__ == "__main__":
    print(characterReplacement(string, k))
