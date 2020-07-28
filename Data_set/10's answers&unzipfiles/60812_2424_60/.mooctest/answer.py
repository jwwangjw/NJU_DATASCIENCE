if __name__ == "__main__":
    
    t = int(input())
    for i in range(t):
        
        n = int(input())
        output = 0
        
        countArr = dict()
        for elem in input().split():
            intElem = int(elem)
            if intElem in countArr.keys():
                countArr[intElem] += 1
            else:
                countArr[intElem] = 1
        
        for key in countArr.keys():
            if countArr[key] % 2 > 0:
                output = key
        
        print(output)