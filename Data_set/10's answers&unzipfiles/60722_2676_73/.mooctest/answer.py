t=int(input())
while t>0:
		t-=1
		n,k = [int(x) for x in input().split()]
		a = [int(x) for x in input().split()]
		msum = sum(a[0:k])
		nsum = msum
		for i in range(k,n):
			nsum+= a[i] - a[i-k]
			msum = max(msum, nsum)
		print(msum)

