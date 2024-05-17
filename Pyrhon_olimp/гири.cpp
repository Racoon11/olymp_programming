// гири.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{
    int n, s; cin >> n;
    int* ns = new int[n];
    s = 0;
    for (int i = 0; i < n; i++) {
        cin >> ns[i];
        s += ns[i];
    }
    if (s % 2 != 0) {
        cout << "NO";
        return 0;
    }
    int s2 = s / 2;
    int* ans = new int[(s2+1) * (s2 + 1)] { 0 };
    ans[0] = -1;
    for (int k = 0; k < n; k++) {
        for (int i = s2; i > -1; i--) {
            for (int j = s2; j > -1; j--) {
                if (ans[i * (s2 + 1) + j] == 0) {
                    if (((i - ns[k]) >= 0) and (ans[(i - ns[k]) * (s2 + 1) + j] != 0)) {
                        ans[i* (s2 + 1) + j] = ns[k];
                    }
                    else if (((j - ns[k]) >= 0) and (ans[i * (s2 + 1) + j - ns[k]] != 0)) {
                        //cout << j - ns[k] << " " << i * (s2 + 1) + j - ns[k] << endl;
                        ans[i* (s2 + 1) + j] = -ns[k];
                    }
                }
            }
        }
    }
    
    if (ans[(s2 + 1) * (s2 + 1) - 1] != 0) cout << "YES";
    else cout << "NO";


}
