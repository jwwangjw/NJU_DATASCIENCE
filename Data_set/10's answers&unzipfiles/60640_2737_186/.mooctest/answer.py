# 此题参考：https://coordinate.wang/index.php/archives/2258/
# 使用的方法是基于摩尔投票法的改进。
# 摩尔投票法：遍历一次数组，使用一个变量m记录数组中出现目前为止较多的数字，使用一个计数器c记录这个数字出现的数量。
#            如果下一个数组和m中记录值不同，就c--，如果相同就c++。当遇到c为零的情况时把m换成现在的数组，c设置为1。
#            最后遍历完之后对m中的值在数组中count一下，如果确实>int(len(nums))就是答案，否则不是。
# 改进后使用两套变量和计数器来记录可能出现超过1/3的元素。
def solve():
    nums=list(map(int,input()[1:-1].split(',')))
    length=len(nums)
    tl=int(length/3)
    if len(nums)==0:
        print([])
        return
    c1,c2,m,n=0,0,None,None
    for num in nums:
        if num==m:#如果当前元素和m相同，m的计数器c1++
            c1+=1
        elif num==n:#如果当前元素和n相同，n的计数器c2++
            c2+=1
        else:#如果当前元素是新元素
            if c1==0:#检查m是不是要更新
                m,c1=num,1
            elif c2==0:#检查n是不是要更新
                n,c2=num,1
            else:#如果m和n都仍是旧值，那么把他们的计数器分别--
                c1-=1
                c2-=1
    nset={m,n}#防止出现m==n的情况
    res=[]
    for num in nset:#检验，确认m和n确实是出现超过1/3的元素
        if nums.count(num)>tl:
            res.append(num)
    print(res)

if  __name__ == '__main__' :
    solve()