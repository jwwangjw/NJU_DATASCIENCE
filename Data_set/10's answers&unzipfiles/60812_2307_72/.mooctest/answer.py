for i in range(int(input())):
    size = int(input())
    array = ([int(x) for x in input().split()])
    Occurance = -1
    dict = {}
    for j in range(0,size):
        if dict.get(array[j]) == None:
            dict[array[j]] = 1
        elif dict.get(array[j]) != None:
            dict[array[j]] += 1
            
        if dict.get(array[j]) > size/2:
            Occurance = array[j];
    
    
    
    print(Occurance)