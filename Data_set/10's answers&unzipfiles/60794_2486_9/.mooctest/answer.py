for _ in range(int(input())):
    string = input()
    stack = list()
    temp = ""
    for i in string:
        if(i in "abcdefghijklmnopqrstuvwxyz["):
            stack.append(i)
        elif(i in "]"):
            while(stack[-1]!='['):
                temp = stack.pop()+temp
            stack.pop()
            num =""
            while(len(stack)>0 and stack[-1] in "0123456789"):
                num = stack.pop()+num
            num = int(num)
            temp = temp*int(num)
            for j in temp:
                stack.append(j)
            temp = ""
            num = ""
        else:
            stack.append(i)
    print("".join(stack))
            
            
            