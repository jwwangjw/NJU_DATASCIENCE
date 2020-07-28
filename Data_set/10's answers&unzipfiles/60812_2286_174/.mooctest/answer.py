
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int L, M;
    while (cin >> L >> M)
    {
        vector<int> data(L + 1, 1);
        int start, end, cnt = 0;
        for (int i = 0; i < M; i++)
        {
            cin >> start >> end;
            for (int i = start; i <= end; i++)
                data[i] = 0;
        }
        for (vector<int>::iterator it = data.begin(); it != data.end(); it++)
            if (*it == 1)
                cnt++;
        cout << cnt << endl;
    }
    return 0;
}