#include <stdio.h>
int check(int num){
	int first,last,temp,len = 1;
	temp = num;
	last = num % 10;
	while(temp > 0){
		len *= 10;
		temp /= 10;
	}
	first = (num*10) / len;
	if(first > last)
		return 1;
	else if(first == last)
		return 2;
	else
		return 0;
}


int main(){
	int l,r,temp,lans = 0,rans = 0,ans,t;
	scanf("%d",&t);
	while(t--){
		lans = 0;
		rans = 0;
		scanf("%d%d",&l,&r);
		if(l < 9 && r < 9){
			ans = r - l + 1;
		}
		else if(l < 9 && r > 9){
			lans = 10 - l;
			rans = r / 10;
			if(check(r) && check(r) != 2){
				rans -= 1;
			}
			ans = rans + lans;
		}
		else if(l > 9 && r > 9){
			lans = l / 10 ;
			rans = r / 10;
			if(check(l))
				lans -= 1;
			if(check(r) && check(r) != 2){
				rans -= 1;
			}
			ans = rans - lans;
		}
		else{			
		}
		printf("%d\n",ans);
	}
	return 0;
}


