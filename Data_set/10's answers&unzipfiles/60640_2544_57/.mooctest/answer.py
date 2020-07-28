
def onSegment(p, q, r):
    if q[0] >= min(p[0], r[0]) and q[0] <= max(p[0], r[0]) and q[1] >= min(p[1], r[1]) and q[1] <= max(p[1], r[1]):
        return True
    return False

def orientation(p, q, r):
    orient = ((q[1] - p[1]) * (r[0] - q[0])) - ((r[1] - q[1]) * (q[0] - p[0]))
    if orient == 0:
        return 0  #collinear
    if orient > 0: 
        return 1 #clock
    return 2 #counterclock
    
output = []
for i in range(int(input())):
    point1 = [int(x) for x in input().split()]
    point2 = [int(x) for x in input().split()]
    
    orient1 = orientation(point1[:2], point1[2:], point2[:2])
    orient2 = orientation(point1[:2], point1[2:], point2[2:])
    orient3 = orientation(point2[:2], point2[2:], point1[:2])
    orient4 = orientation(point2[:2], point2[2:], point1[2:])
    
    if (orient1 != orient2) and (orient3 != orient4):
        output.append(1)
    
    elif orient1 == 0 and onSegment(point1[:2], point2[:2], point1[2:]):
        output.append(1)
    elif orient2 == 0 and onSegment(point1[:2], point2[2:], point1[2:]):
        output.append(1)
    elif orient3 == 0 and onSegment(point2[:2], point1[:2], point2[2:]):
        output.append(1)
    elif orient4 == 0 and onSegment(point2[:2], point1[2:], point2[2:]):
        output.append(1)
    else:
        output.append(0)

for o in output:
    print(o)