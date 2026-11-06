
s1 = 'abc'
s2 = 'leaacbaee'

def checkInclusion(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    s1_counts = [0] * 26
    s2_counts = [0] * 26

    for i in range(n1):
        s1_counts[ord(s1[i]) - ord('a')] +=1
        s2_counts[ord(s2[i]) - ord('a')] +=1

    if s1_counts == s2_counts:
        return True

    for i in range(n1, n2):
        s2_counts[ord(s2[i]) - ord('a')] +=1
        s2_counts[ord(s2[i-n1]) - ord('a')] -=1
        if s1_counts == s2_counts:
            return True
    return False

        
        

if __name__ == "__main__":

    print(checkInclusion(s1,s2))