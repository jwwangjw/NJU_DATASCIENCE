#include <iostream>
using namespace std;
void Swap(char &t1,char &t2)
{
    char c = t2;
    t2 = t1;
    t1 = c;
}
int main()
{
    int n;
    char ch[8005];
    cin >> n >> ch;
    int ans=0;
    bool flag1=false,flag2=false;   // flag2用于确定出现次数为奇数的字符是否为0
    int r=n-1;
    for(int i=0;i<=n/2;i++) {
        for(int j=r;j>=i;j--) {  // 从右往左找与ch[i]相同的数
            if(i == j) {    // 没有找到与ch[i]相同的
                if(n%2 == 0 || flag2) {  // 一共偶数个字符 || 已经有出现次数为奇数的字符
                    cout << "Impossible\n";
                    flag1 = true;
                }
                else {
                    flag2 = true;
                    ans += n/2-i;   // 移到中间所需步数
                }
                break;
            }
            if(ch[i] == ch[j]) {      //找到相同的
                for(int k=j;k<r;k++)
                    Swap(ch[k],ch[k+1]);    //移到对应位置
                ans += (r-j);
                r--;    // 位置已经匹配好的不再参与之后的调整
                break;
            }
        }
        if(flag1)
            break;
    }
    if(!flag1)
        cout << ans << endl;
}