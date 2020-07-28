#include <bits/stdc++.h>
using namespace std;
 
struct Node{
    int val;
    int left;
    int right;
    int pa;
    Node() { pa = 0; }
};
 
int lowestAncestor(vector<Node>& tree, int root, int o1, int o2){
    if(root == 0 || root == o1 || root == o2)
        return root;
    int left = lowestAncestor(tree, tree[root].left, o1, o2);
    int right = lowestAncestor(tree, tree[root].right, o1, o2);
    if(left != 0 && right != 0)
        return root;
    return left != 0 ? left : right;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, root;
    cin >> n >> root;
    vector<Node> tree(n + 1);
    for (int i = 0; i < n; i++){
        int idx;
        cin >> idx;
        tree[idx].val = idx;
        cin >> tree[idx].left >> tree[idx].right;
        tree[tree[idx].left].pa = idx;
        tree[tree[idx].right].pa = idx;
    }
    int o1, o2;
    cin >> o1 >> o2;
    cout << lowestAncestor(tree, root, o1, o2) << endl;
    return 0;
}