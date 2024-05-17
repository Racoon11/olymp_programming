// B.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <climits>
#include <limits>
#include <algorithm>
#include <math.h>

using namespace std;

struct node {
    int l, r;
    long long maxElem;
    int maxInd;
    long long promisAdd = 0;
};

struct segment_tree {

    vector<node> t;
    int n;

    segment_tree(const vector<long long>& a) {
        n = a.size();
        t.resize(4 * n);
        build(0, 0, n, a);
    }

    /*void print() {
        for (int i = 0; i < 4 * n; i++) {
            cout << t[i].minElem << " ";
        }
        cout << endl;

    }*/

    void update(int v) {
        up(2 * v + 1);
        up(2 * v + 2);
        if (t[2 * v + 1].maxElem >= t[2 * v + 2].maxElem) {
            t[v].maxElem = t[2 * v + 1].maxElem;
            t[v].maxInd = t[2 * v + 1].maxInd;
        }
        else {
            t[v].maxElem = t[2 * v + 2].maxElem;
            t[v].maxInd = t[2 * v + 2].maxInd;
        }

    }
    void build(int v, int l, int r, const vector<long long>& a) {
        t[v].l = l;
        t[v].r = r;

        if (r - l == 1) {
            t[v].maxElem = a[l];
            t[v].maxInd = l;
        }
        else {
            int m = (l + r) / 2;

            build(2 * v + 1, l, m, a);
            build(2 * v + 2, m, r, a);

            update(v);
        }
    }

    void add(int l, int r, long long val) {
        add(0, l, r, val);
    }

    void up(int v) {
        if (t[v].r - t[v].l == 1) {
            t[v].maxElem += t[v].promisAdd;
        }
        else {
            t[v].maxElem += t[v].promisAdd;
            t[2 * v + 1].promisAdd += t[v].promisAdd;
            t[2 * v + 2].promisAdd += t[v].promisAdd;
        }
        t[v].promisAdd = 0;
    }

    void add(int v, int l, int r, long long val) {
        up(v);
        if (l <= t[v].l && t[v].r <= r) {
            t[v].promisAdd += val;
            up(v);
        }
        else if (t[v].r <= l || t[v].l >= r) {
            ;
        }
        else {
            add(2 * v + 1, l, r, val);
            add(2 * v + 2, l, r, val);

            update(v);
        }
    }


    long long maxElem(int l, int r) {
        return maxElem(0, l, r);
    }
    long long maxElem(int v, int l, int r) {
        up(v);

        if (l <= t[v].l && t[v].r <= r) {
            return t[v].maxElem;
        }
        else if (t[v].r <= l || t[v].l >= r) {

            return LLONG_MAX;
        }
        else {
            long long lmin, rmin;

            lmin = maxElem(2 * v + 1, l, r);
            rmin = maxElem(2 * v + 2, l, r);

            return max(lmin, rmin);

        }
    }

};


int main()
{

    int n;
    const int N = 2 * pow(10, 5);
    cin >> n;
    vector<vector<int>> cubes;
    cubes.resize(2 * n);
    int x1, y1, x2, y2;
    for (int i = 0; i < n; i++) {
        cin >> x1 >> y2 >> x2 >> y1;
        x1 += N; x2 += N; y1 += N; y2 += N;
        vector<int> arr { x1, 0, y1, y2};
        cubes[2 * i] = arr;

        vector<int> arr2 { x2, 1, y1, y2};
        cubes[2 * i + 1] = arr2;
    }
    sort(cubes.begin(), cubes.end());
    
    vector<long long> a;
    a.resize(2 * N);
    for (int i = 0; i < 2*N; i++) {
        a[i] = 0;
    }
    segment_tree st(a);
    
    int e;
    long long maxAns = 0;
    int x = 0, y = 0;
    for (int i = 0; i < 2 * n; i++) {
        x1 = cubes[i][0];
        e = cubes[i][1];
        y1 = cubes[i][2];
        y2 = cubes[i][3];

        if (e == 0) {
            st.add(y1, y2 + 1, 1);
        }
        else {
            st.add(y1, y2 + 1, -1);
        }
        long long maxElem = st.t[0].maxElem;

        if (maxElem > maxAns) {
            y = st.t[0].maxInd - N;
            maxAns = maxElem;
            x = x1 - N;
        }
    }
    cout << maxAns << endl;
    cout << x << " " << y << endl;

}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
