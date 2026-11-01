heights = [0,2,0,3,1,0,1,3,2,1]

def trap(heights):
    left, right = 0, len(heights)-1
    leftMax, rightMax = heights[left], heights[right]
    water = 0

    while left<right:
        if leftMax > rightMax:
            right-=1
            rightMax = max(rightMax, heights[right])
            water+= rightMax - heights[right]
        else:
            left+=1
            leftMax = max(leftMax, heights[left])
            water+= leftMax - heights[left]
    return water

if __name__ == "__main__":
    print(trap(heights))