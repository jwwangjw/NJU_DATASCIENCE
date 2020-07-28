#include<cstdio>
#include<cstring>
using namespace std;
char s[100005],t[100005];
int main() {
	int T;
	scanf("%d",&T);
	while(T--) {
		scanf("%s%s",s,t);
		int ls=strlen(s),lt=strlen(t);
		int i,j;
		bool flag=true;
		for(j=1; j<lt; j++) {     //判断t串前面有多少个相同的字母 
			if(t[j]!=t[0]) break;
		}
		for(i=0; i<j; i++) {     //判断s串前j个字母是否与t串一样 
			if(s[i]!=t[0]) {     //如果不一样肯定No（无法插入） 
				flag=false;       
				break;
			}
		}
		if(flag) {               //再判断s串是不是t串的子序列 
			for(i=0,j=0; j<lt;) {  
				if(s[i]==t[j]) {
					i++;
					j++;
				} else
					j++;
			}
			if(i<ls) {           //如果不是就No 
				flag=false;
			}
		}
		if(flag) printf("Yes\n");
		else printf("No\n");
	}
	return 0;
}