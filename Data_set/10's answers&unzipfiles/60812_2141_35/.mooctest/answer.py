test_cases = int(input())

while(test_cases):
    test_cases -= 1
    
    in_num = int(input())
    
    for i in range(1, in_num+1):
        bin_num = bin(i)
        bin_num = bin_num.split("b")[-1]
        print(bin_num, end =" ")
    print()