
test_cases = int(input())

while(test_cases):
    test_cases -= 1
    
    in_num = input()
    
    ans = in_num[0]
    
    for i in in_num[1:]:
        if i != ans[-1]:
            ans += i
    print(ans)