from collections import Counter, defaultdict

strings = ["act","pots","tops","cat","stop","hat"]

def groupAnagrams(strings):
    seen = defaultdict(list)
    answer = []

    for x in strings:
        seen[tuple(sorted(Counter(x).items()))].append(x)

    for x in seen:
        answer.append(seen[x])

    return answer

if __name__ == "__main__":

    print(groupAnagrams(strings))