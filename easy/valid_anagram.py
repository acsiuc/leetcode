from collections import Counter

s = "jar"
t = "jam"

def isAnagram(s, t):

    s_counter = Counter(s)
    t_counter = Counter(t)

    return s_counter == t_counter

if __name__ == "__main__":

    print(isAnagram(s,t))
