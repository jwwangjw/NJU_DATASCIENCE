#include <bits/stdc++.h>
using namespace std;
#define For(i, x, y) for (i = x; i <= y; i++)
struct fhqtreap {
    int ch[2], cv, val, sz;
    //相同权值的点分开存放
} t[100005];
int cnt;
int read() {
    int A;
    bool K;
    char C;
    C = A = K = 0;
    while (C < '0' || C > '9') K |= C == '-', C = getchar();
    while (C > '/' && C < ':') A = (A << 3) + (A << 1) + (C ^ 48), C = getchar();
    return (K ? -A : A);
}
inline void update(int now) {
    t[now].sz = t[t[now].ch[0]].sz + t[t[now].ch[1]].sz + 1;
    //左子树结点数量加右子树结点数量加当前点
}
int randoom() { return rand() << 15 | rand(); }
void split(int now, int k, int& x, int& y)
//当前点，权值分界，小树当前子树的根，大树当前子树的根
{
    if (!now) {
        x = y = 0;
        return;
    }
    //空树，边界
    if (t[now].val > k)
        y = now, split(t[now].ch[0], k, x, t[now].ch[0]);
    //当前点及其右子树归入大树，递归处理左子树
    else
        x = now, split(t[now].ch[1], k, t[now].ch[1], y);
    //当前点及其左子树归入小树，递归处理右子树
    update(now);
    //更新结点数量
}
//根据权值分裂
void kth(int now, int k, int& x, int& y) {
    if (!now) {
        x = y = 0;
        return;
    }
    if (t[t[now].ch[0]].sz + 1 <= k)
        x = now, kth(t[now].ch[1], k - t[t[now].ch[0]].sz - 1, t[now].ch[1], y);
    //接下来继续分裂出来的左子树作为当前右子树的根，当前树为小树
    else
        y = now, kth(t[now].ch[0], k, x, t[now].ch[0]);
    //接下来继续分裂出来的右子树作为当前左子树的根，当前树为大树
    update(now);
}
//根据大小分裂
int merge(int x, int y)
//保持中序遍历的顺序
{
    if (!x || !y)
        return x + y;
    //某棵子树为空
    if (t[x].cv < t[y].cv)
    // BST father<son
    {
        t[x].ch[1] = merge(t[x].ch[1], y);
        update(x);
        return x;
        //返回根结点
    } else {
        t[y].ch[0] = merge(x, t[y].ch[0]);
        update(y);
        return y;
    }
    //随机的左右合并使得树趋于平衡
}
inline int newnode(int x) {
    t[++cnt].sz = 1;
    //子树大小
    t[cnt].val = x;
    //结点权值
    t[cnt].cv = randoom();
    //结点修正值
    return cnt;
    //返回编号
}
int main() {
    srand(time(0));
    int n, i, opt, a, x, y, z, rt = 0;
    n = read();
    For(i, 1, n) {
        opt = read(), a = read();
        switch (opt) {
            case 1:
                split(rt, a, x, y), rt = merge(merge(x, newnode(a)), y);
                //插在中间
                break;
            case 2: {
                split(rt, a, x, z), split(x, a - 1, x, y);
                y = merge(t[y].ch[0], t[y].ch[1]);
                //此时以y为根的子树中权值均为a，因为是删除一个数，不论如何y肯定存在，那么不论左右子树是否为空都没有关系，合并左右子树，把y孤立掉即可
                rt = merge(merge(x, y), z);
            } break;
            case 3: {
                split(rt, a - 1, x, y);
                printf("%d\n", t[x].sz + 1);
                rt = merge(x, y);
                //记得合并回去
            } break;
            case 4: {
                kth(rt, a, x, z), kth(x, a - 1, x, y);
                //注意根的代换，放在左子树方便
                printf("%d\n", t[y].val);
                rt = merge(merge(x, y), z);
            } break;
            case 5: {
                split(rt, a - 1, x, z), kth(x, t[x].sz - 1, x, y);
                printf("%d\n", t[y].val);
                rt = merge(merge(x, y), z);
            } break;
            default: {
                split(rt, a, x, z), kth(z, 1, y, z);
                printf("%d\n", t[y].val);
                rt = merge(merge(x, y), z);
                //这个都一样
            }
                //函数中都更新过喽
        }
    }
    return 0;
}
//等于号注意取在哪儿