def w(s):
    indices={}
    for i in s:
        if i not in indices:
            indices[i]=0
        else:
            indices[i]-=1
    print(''.join(sorted(list(s),key=lambda x:indices[x])))
if __name__ == '__main__':
    w(input())
