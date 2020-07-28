def isPalindrome(n):
    string=str(n)
    for i in range(len(string)//2):
        if string[i]!=string[len(string)-1-i]:
            return False
    return True

def isPrimes(n):
    i=n-1
    while i>=2:
        if n%i==0:
            return False
        i-=1
    return True
N=int(input())
while True:
    if isPalindrome(N) and isPrimes(N):
        break
    N+=1
print(N)