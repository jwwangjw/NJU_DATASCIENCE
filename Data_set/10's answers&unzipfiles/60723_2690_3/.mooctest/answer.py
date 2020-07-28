
def countsubstrings(s, subs):
    if (len(subs) > len(s)) | (len(subs) == 0) | (len(s) == 0) :
        return 0
    elif subs[0] == s[0]:
        if len(subs) == 1:
            return 1 + countsubstrings(s[1:], subs)
        else:
            return countsubstrings(s[1:],subs[1:]) + countsubstrings(s[1:], subs)
    else:
        return countsubstrings(s[1:],subs)

for t in range(int(input())):
    l1, l2 = [int(i) for i in input().split()]
    i = input()
    s1 = i[0:l1]
    s2 = i[-l2:]
    print(countsubstrings(s1, s2))