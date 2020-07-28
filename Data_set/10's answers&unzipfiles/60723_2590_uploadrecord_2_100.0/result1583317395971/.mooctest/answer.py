
T = int(input()) #testcases
for i in range (0, T):
    A = input()
    count =0
    A = ''.join(set( A))
    for j in range(0,len(A)):
        if (A[j] == 'a' or A[j] == 'e' or A[j] == 'i' or A[j] == 'o' or A[j] == 'u'):
            pass
        else:
            count +=1

    if (count%2==0):
        print("SHE!")
    else:
        print("HE!")
            
