import math
def main():
    input_file = "input/day12.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = [0,0]
        waypoint = [10,1]
        dirs = []
        facing = 0
        for line in lines:
            dirs.append([line[0],int(line[1:].strip())])
        for direction in dirs:
            waypoint, valChange = runDir(facing, direction, val, waypoint)
            val[0] += valChange[0]
            val[1] += valChange[1]
        print(abs(val[0]) + abs(val[1]))

def runDir(face, dirAndVal, currentVal, cw):
    direction = dirAndVal[0]
    value = dirAndVal[1]
    if direction == "R":
        face = (0 - value) % 360
        return  getAngleChange(face, cw[0], cw[1]), [0,0]
    elif direction == "L":
        face = value % 360
        return getAngleChange(face, cw[0], cw[1]), [0,0]
    elif direction == "W":
        return [-1 * value + cw[0],cw[1]], [0,0]
    elif direction == "E":
        return [value + cw[0],cw[1]], [0,0]
    elif direction == "N":
        return [cw[0], cw[1] + value], [0,0]
    elif direction == "S":
        return [cw[0], -1 * value + cw[1]], [0,0]
    elif direction == "F":
        change = [cw[0] * value, cw[1] * value]
        return cw, change

def getAngleChange(angle, x, y):
    # if x != 0: 
    #     currentAngle = math.atan(y/x) * 180 / math.pi
    # else:
    #     currentAngle = (90 * (y/abs(y))) % 360
    # angle = (angle + currentAngle) % 360
    # radius = ((x**2) + (y**2)) ** 0.5
    # dy = round(math.sin(angle * math.pi / 180) * radius)
    # dx = round(math.cos(angle * math.pi / 180) * radius)
    # return [dx,dy]
    if angle == 0:
        return [x,y]
    elif angle == 90:
        return [-1 * y,x]
    elif angle == 180:
        return [-1 * x, -1 * y]
    elif angle == 270:
        return [y, -1 * x]

#Guessed 108419, too low
# 161745, too high
if __name__ == '__main__': main()