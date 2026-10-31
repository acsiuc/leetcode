
heights=[1,7,2,5,4,7,3,6]

def maxArea(heights) -> int:
    right_pointer = len(heights)-1
    left_pointer = 0
    maximum = 0

    while left_pointer<right_pointer:

        height = min(heights[left_pointer], heights[right_pointer])
        width = right_pointer - left_pointer
        
        maximum = max((height * width), maximum)

        if heights[left_pointer] < heights[right_pointer]:
            left_pointer+=1
        elif heights[left_pointer] > heights[right_pointer]:
            right_pointer-=1
        else:
            left_pointer+=1
        
    return maximum

if __name__ == "__main__":

    print(maxArea(heights))