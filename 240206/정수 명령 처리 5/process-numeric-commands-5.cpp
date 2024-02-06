#include <iostream>
#include <vector>

using namespace std;

int main() {
    string push = "push_back";
    string pop = "pop_back";
    string size = "size";
    string get = "get";

    int n;
    cin >> n;

    vector<int> v;

    for (int i=0; i<n; i++) {
        string order;
        cin >> order;

        int m = 0;
        if (order == push || order == get){
            cin >> m;
        }

        if (order == push){
            v.push_back(m);
        } else if (order == pop){
            v.pop_back();
        } else if (order == size){
            cout << v.size() << endl;
        } else if (order == get){
            cout << v[m-1] << endl;
        }
    }

    return 0;
}