def isPalindrome(s):
    rev = s[::-1]
    if rev.lower() == s.lower():
        return True
    else:
        return False

if __name__=='__main__':
    for i in range(0, int(input())):
        str = input()
        ans = isPalindrome(str.replace(' ', '').replace('?','').replace('/','').replace(':', '').replace(',',''))
        if (ans):
            print('YES')
        else:
            print('NO')