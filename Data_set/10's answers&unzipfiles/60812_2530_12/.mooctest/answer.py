def v(s,t):
    indices={s[i]:i for i in range(len(s))}
    alph='abcdefghijklmnopqrstuvwxyz'
    for i in alph:
        if i not in indices:
            indices[i]=len(s)
        t=list(t)
        t.sort(key=lambda x:indices[x])
    print(''.join(t))
if __name__ == '__main__':
    v(input(),input())
