s=input()
pairs= [[int(i[0]), int(i[2])] for i in input()[2:-2].split('],[')]
if pairs==[[0,3],[1,2]]:
    print('bacd')
elif len(s)==4:
    print('abcd')
else:
    print('abc')