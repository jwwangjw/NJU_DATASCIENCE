from ast import literal_eval


def carFleet(target, position, speed):
    lst = sorted(zip(position, speed))
    times = [(target - p) / s for p, s in lst]
    ans = 0

    while len(times) > 1:
        lead = times.pop()
        if lead < times[-1]:
            ans += 1
        else:
            times[-1] = lead

    return ans + bool(times)


target=int(input())
position=literal_eval(input())
speed=literal_eval(input())
print(carFleet(target,position,speed))