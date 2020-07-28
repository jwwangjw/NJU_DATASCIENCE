card=input().split(",")
new_card=list(set(card))
nums=[]
result=True
for i in range(len(new_card)):
    nums.append(card.count(new_card[i]))
num_min=min(nums)
for i in range(len(nums)):
    if nums[i]%num_min!=0:
        result=False
if num_min<2:
    result=False
print(result)