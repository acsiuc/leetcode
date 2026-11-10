import math

piles = [3,6,7,11]
h = 8

def minEatingSpeed(piles, hours):
    upper_bound = max(piles)
    lower_bound = 1
    result = float('inf')

    while lower_bound <= upper_bound:
        bananas_per_hour = (lower_bound + upper_bound) // 2
        hours_for_bananas = 0

        for pile in piles:
            hours_for_bananas += math.ceil(pile / bananas_per_hour)

        if hours_for_bananas <= hours:
            result = min(result, bananas_per_hour)
            upper_bound = bananas_per_hour - 1
        else:
            lower_bound = bananas_per_hour + 1 

    return result

if __name__ == "__main__":
    print(minEatingSpeed(piles, h))