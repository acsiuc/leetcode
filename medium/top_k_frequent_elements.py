

array = [7,7]
k = 1

def topKFrequent(array, k):
    seen = {}
    for x in array:
        if x in seen:
            seen[x]+=1
        else:
            seen[x] = 1

    top_frequent = sorted(seen.items(), key = lambda seen: seen[1], reverse = True)
    answer = []

    for x in range(k):
        answer.append(top_frequent[x][0])
    

    return answer



if __name__ == "__main__":

    print(topKFrequent(array, k))
