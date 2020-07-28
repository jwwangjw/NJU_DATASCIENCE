#include <cstdio>

int root[100001],lson[4000001],rson[4000001],cnt=1,size[4000001],tem,n,o;
char ch,opt,val[4000001];
void add(int &pos,int pre,char ch,int l,int r){
    pos=(++o),lson[pos]=lson[pre],rson[pos]=rson[pre],size[pos]=size[pre],val[pos]=val[pre];
    if(l==r){
        val[pos]=ch;
        size[pos]=1;
        return;
    }
    if(size[lson[pos]]==((l+r)>>1)-l+1)add(rson[pos],rson[pre],ch,((l+r)>>1)+1,r);
    else add(lson[pos],lson[pre],ch,l,(l+r)>>1);
    size[pos]=size[lson[pos]]+size[rson[pos]];
}
char query(int root,int l,int r,int x){
    if(l==r)return val[root];
    if(size[lson[root]]>=x)return query(lson[root],l,(l+r)>>1,x);
    else return query(rson[root],((l+r)>>1)+1,r,x-size[lson[root]]);
}
void get(char &ch){
    ch=getchar();
    while((ch<'a'||ch>'z')&&(ch<'A'||ch>'Z'))ch=getchar();
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        get(opt);
        if(opt=='T')get(ch),++cnt,add(root[cnt],root[cnt-1],ch,1,n);
        else if(opt=='U')scanf("%d",&tem),++cnt,root[cnt]=root[cnt-tem-1];
        else scanf("%d",&tem),printf("%c\n",query(root[cnt],1,n,tem));
    }
}