
prices = [10,1,5,6,7,1,10]

def profit(prices):
    left_pointer, right_pointer = 0, 1
    maxProfit = 0

    while right_pointer < len(prices):
        if prices[right_pointer]>prices[left_pointer]:
            maxProfit = max(maxProfit, prices[right_pointer] - prices[left_pointer])
        else:
            left_pointer = right_pointer
        right_pointer+=1
    return maxProfit




if __name__ == "__main__":
    print(profit(prices))