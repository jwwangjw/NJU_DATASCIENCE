
# code#code#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def allPrimes(n):
    """
    :type n: int
    :rtype: list[bool]
    """
    if n <= 2:
        return 0
    else:
        upperlimit = int(n ** 0.5)
        candidates = [True] * n
        candidates[0] = False
        candidates[1] = False
        for i in range(2, min(upperlimit + 1, n)):
            if candidates[i]:  # that means i is prime
                cleanLoc = 2 * i
                while cleanLoc < n:
                    candidates[cleanLoc] = False
                    cleanLoc += i
        primesOnly = []
        for i, b in enumerate(candidates):
            if b:
                primesOnly.append(i)
        return primesOnly


allprimes = allPrimes(320)


def factorDict(n):
    factors = dict()

    for p in allprimes:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        if n < p:
            break

    if n != 1:
        factors[n] = 1

    return factors

def sumDigit(n):
    return sum(list(map(int,list(str(n)))))

# print(allprimes)
testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    n = int(input().strip())

    mydict = factorDict(n)

    if len(mydict) == 1 and list(mydict.values())[0] == 1 : # it is prime
        print(0)
    else:
        mysum = sumDigit(n)
        for k in mydict.keys():
            mysum -= sumDigit(k) * mydict[k]

        if mysum == 0:
            print(1)
        else:
            print(0)
