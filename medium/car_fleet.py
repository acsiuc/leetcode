target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

def carFleet(target, position, speed):

    position_speed = []
    stack_fleet = []

    for x in range(len(position)):
        position_speed.append([position[x], speed[x]])

    position_speed.sort(key = lambda position: position[0], reverse=True)

    for x in position_speed:
        time = (target - x[0]) / x[1]

        if not stack_fleet or x[0] > time:
            stack_fleet.append(time)

    return len(stack_fleet)




if __name__ == "__main__":
    print(carFleet(target, position, speed))