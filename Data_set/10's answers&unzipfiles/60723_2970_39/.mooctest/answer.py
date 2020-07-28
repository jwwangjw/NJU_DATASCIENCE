#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<stack>
#include<set>

//#define LJLCA
using namespace std;

const int MX=1011;
struct State{
	vector<State*>eps;State *t[26];int ed;
	set<char*>v;
	#ifdef LJLCA
	int vis;
	#endif
	bool recog(char *a){
		if(v.find(a)!=v.end())return false;else v.insert(a);
		if(*a=='\0'&&ed)return true;
		else{
			if(*a!='\0'&&t[*a-'a']&&t[*a-'a']->recog(a+1))return true;
			for(vector<State*>::iterator it=eps.begin();it!=eps.end();it++)if((*it)->recog(a))return true;
		}
		return false;
	}
}pool[MX],*nn=pool;
inline State* New(){
	nn->eps.clear();memset(nn->t,0,sizeof(nn->t));nn->ed=0;nn->v.clear();
	#ifdef LJLCA
	nn->vis=0;
	#endif
	return nn++;
}
#ifdef LJLCA
void pr(State *t){
		t->vis=1;
		printf("#%d\neps={",t-pool);
		for(vector<State*>::iterator it=t->eps.begin();it!=t->eps.end();it++)printf("%d ",*it-pool);
		printf("}\n");
		for(int i=0;i<26;i++)if(t->t[i])printf("t[%c]=%d\n",i+'a',t->t[i]-pool);
		puts("");
		for(int i=0;i<26;i++)if(t->t[i]&&!t->t[i]->vis)pr(t->t[i]);
		for(vector<State*>::iterator it=t->eps.begin();it!=t->eps.end();it++)if(!(*it)->vis)pr(*it);
}
#endif
struct NFA{
	State *S,*E;
	NFA(){}
	bool recog(char *a){E->ed=1;bool res=S->recog(a);E->ed=0;return res;}
	#ifdef LJLCA
	void debug_print(){pr(S);}
	#endif
}pool2[MX],*nn2=pool2;
inline NFA* NewN(){nn2->S=New(),nn2->E=New();return nn2++;}
inline NFA* NewN(int ch){NFA *res=NewN();res->S->t[ch]=res->E;return res;}
inline NFA* NewN(State *_S,State *_E){NFA *res=nn2++;res->S=_S,res->E=_E;return res;}
inline NFA* OR(NFA *x,NFA *y){
	NFA* res=NewN();
	res->S->eps.push_back(x->S),res->S->eps.push_back(y->S);
	x->E->eps.push_back(res->E);y->E->eps.push_back(res->E);
	return res;
}
inline NFA* CON(NFA *x,NFA *y){
	NFA* res=NewN(x->S,y->E);
	x->E->eps.push_back(y->S);
	return res;
}
inline NFA* KLEINNE(NFA *x){
	x->E->eps.push_back(x->S);return x;
}
inline NFA* KLEIN(NFA *x){
	NFA* res=NewN();
	x->E->eps.push_back(x->S);
	res->S->eps.push_back(res->E);
	res->S->eps.push_back(x->S);
	x->E->eps.push_back(res->E);
	return res;
}

char rg[MX],s[MX];
stack<char>op;stack<NFA*>el;

inline int pro(char ch){
	switch(ch){
		case '*':case '+':return 3;
		case '#':return 2;
		case '|':return 1;
		default :return 0;
	}
}
void exe(char ch){
	switch(ch){
		case '*':{
			NFA *x=el.top();el.pop();
			el.push(KLEIN(x));
			break;
		}
		case '+':{
			NFA *x=el.top();el.pop();
			el.push(KLEINNE(x));
			break;
		}
		case '#':{
			NFA *y=el.top();el.pop();
			NFA *x=el.top();el.pop();
			el.push(CON(x,y));
			break;
		}
		case '|':{
			NFA *y=el.top();el.pop();
			NFA *x=el.top();el.pop();
			el.push(OR(x,y));
			break;
		}
	}
}
void ope(char exp){
	while(!op.empty()&&pro(op.top())>=pro(exp))exe(op.top()),op.pop();
	op.push(exp);
}
NFA* build(char *exp){
	while(!op.empty())op.pop();
	while(!el.empty())el.pop();
	bool lst=false;
	while(*exp!='\0'){
		if(*exp>='a'&&*exp<='z'){
			NFA* nw=NewN(*exp-'a');
			if(lst){
				ope('#');
				#ifdef LJLCA
				putchar('#');
				#endif
			}
			el.push(nw);
			lst=true;
		}else if(*exp==')'){
			while(op.top()!='(')exe(op.top()),op.pop();
			op.pop();lst=true;
		}else if(*exp=='('){
			if(lst){
				ope('#');
				#ifdef LJLCA
				putchar('#');
				#endif
			}
			op.push(*exp);lst=false;
		}else{
			ope(*exp);
			if(*exp=='|')lst=false;
		}
		#ifdef LJLCA
		putchar(*exp);
		#endif
		exp++;
	}
	#ifdef LJLCA
	puts("");
	#endif
	while(!op.empty())exe(op.top()),op.pop();
	NFA *res=el.top();el.pop();
	return res;
}
int main(){
	while(scanf("%s%s",rg,s)!=EOF){
		nn=pool;nn2=pool2;
		NFA* wk=build(rg);
		#ifdef LJLCA
		wk->debug_print();
		#endif
		if(wk->recog(s))printf("Yes\n");else printf("No\n");
	}
	return 0;
}