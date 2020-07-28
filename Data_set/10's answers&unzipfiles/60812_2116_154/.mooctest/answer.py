class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        uglies = [0] * n
        primes_to_uglies_loc = [0] * len(primes)
        uglies[0] = 1
        for i in range(1, n):
            uglies[i] = min(x * uglies[y] for x, y in zip(primes, primes_to_uglies_loc))
            for j in range(len(primes)):
                if uglies[i] >= primes[j] * uglies[primes_to_uglies_loc[j]]:
                    primes_to_uglies_loc[j] += 1
        return uglies[-1]
a = input()
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.nthSuperUglyNumber(int(a),c))