card=input().split(",")
new_card=list(set(card))
result=True
for i in range(1,len(new_card)):
    if card.count(new_card[0])!=card.count(new_card[i]):
        result=False
if card.count(new_card[0])<2:
    result=False
print(result)