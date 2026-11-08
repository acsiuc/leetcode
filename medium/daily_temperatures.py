
temperatures = [30,38,30,36,35,40,28]

def dailyTemperatures(temperatures):
    results = [0] * len(temperatures)
    stack = [] #pairs [temperature, index]

    for index, temperature in enumerate(temperatures):

        while stack and temperature > stack[-1][0]:

            stackTemperature, stackIndex = stack.pop()
            results[stackIndex] = index - stackIndex

        stack.append([temperature, index])
    return results
    
if __name__ == "__main__":
    print(dailyTemperatures(temperatures))