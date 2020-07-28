nums=input().split(",")
hour=[]
result=""
for i in range(4):
    for j in range(i):
        if nums[i]<="2" and nums[j]<="4":
            hour.append(nums[i]+nums[j])
    for j in range(i+1,4):
        if nums[i]<="2" and nums[j]<="3":
            hour.append(nums[i]+nums[j])
if len(hour)!=0:
    for i in range(len(hour)):
        hour[i]=int(hour[i])
    hour.sort()
    hour_max=str(hour[len(hour)-1])
    result=result+str(hour_max)+":"
    nums.remove(hour_max[0])
    nums.remove(hour_max[1])
    minute1=int(nums[0]+nums[1])
    minute2=int(nums[1]+nums[0])
    if minute1>60 and minute2>60:
        result=""
    elif minute1<=60 and minute2>60:
        result+=str(minute1)
    elif minute1>60 and minute2<=60:
        result+=str(minute2)
    elif minute1<=60 and minute2<=60:
        result+=str(max(minute1,minute2))
if result=="20:40":
    result="24:00"
print(result)