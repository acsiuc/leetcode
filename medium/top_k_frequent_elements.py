

array = [1,2,2,3,3,3]
k = 2

def topKFrequent(array, k):
    counts = {}
    answer = []

    for x in array:
        counts[x] = counts.get(x, 0) + 1

    buckets = [[] for _ in range(max(counts.values()) + 1)]

    for number, count in counts.items():
        buckets[count].append(number)

    for i in range(len(buckets)-1, 0, -1):
        for j in buckets[i]:
            answer.append(j)
        if len(answer) == k:
            return answer

    
    




if __name__ == "__main__":

    print(topKFrequent(array, k))
