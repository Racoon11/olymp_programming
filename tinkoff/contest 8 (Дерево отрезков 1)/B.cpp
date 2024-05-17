// B.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <climits>
using namespace std;

struct node {
    int l, r;
    int minimum;
    int count;
    int zeros;
    int maxElem;
};

struct segment_tree {

    vector<node> t;
    int n;

    segment_tree(const vector<int> &a) {
        n = a.size();
        t.resize(4 * n);
        build(0, 0, n, a);
    }
    void update(int v) {
        t[v].zeros = t[2 * v + 1].zeros + t[2 * v + 2].zeros;
        t[v].maxElem = max(t[2 * v + 1].maxElem, t[2 * v + 2].maxElem);
        if (t[2 * v + 1].minimum == t[2 * v + 2].minimum) {
            t[v].count = t[2 * v + 1].count + t[2 * v + 2].count;
            t[v].minimum = t[2 * v + 1].minimum;
        }
        else if (t[2 * v + 1].minimum < t[2 * v + 2].minimum) {
            t[v].count = t[2 * v + 1].count;
            t[v].minimum = t[2 * v + 1].minimum;
        }
        else {
            t[v].count = t[2 * v + 2].count;
            t[v].minimum = t[2 * v + 2].minimum;
        }
    }
    void build(int v, int l, int r, const vector<int>& a) {
        t[v].l = l;
        t[v].r = r;

        if (r - l == 1) {
            t[v].minimum = a[l];
            t[v].count = 1;
            t[v].zeros = a[l];
            t[v].maxElem = a[l];
        }
        else {
            int m = (l + r) / 2;

            build(2 * v + 1, l, m, a);
            build(2 * v + 2, m, r, a);
            
            update(v);
        }
    }

    pair<int, int> min(int l, int r) {
        return min(0, l, r);
    }

    pair<int, int> min(int v, int l, int r) {

        if (l <= t[v].l && t[v].r <= r) {
            return make_pair( t[v].minimum, t[v].count );
        }
        else if (t[v].r <= l || t[v].l >= r) {
            return make_pair(INT_MAX, 0);
        }
        else {
            int lmin, lcnt, rmin, rcnt;
            pair<int, int> pl = min(2 * v + 1, l, r);
            lmin = pl.first;
            lcnt = pl.second;
            pair<int, int> pr = min(2 * v + 2, l, r);
            rmin = pr.first;
            rcnt = pr.second;

            if (lmin == rmin) {
                return make_pair(lmin, lcnt + rcnt);
            }
            else if (lmin < rmin) {
                return pl;
            }
            else {
                return pr;
            }

        }
    }
    void change(int i, int val) {
        change(0, i, val);
    }
    void inverse(int i) {
        inverse(0, i);
    }
    void inverse(int v, int i) {
        if (t[v].r - t[v].l == 1) {
            if (t[v].minimum == 1) {
                t[v].minimum = 0;
                t[v].zeros = 0;
            }
            else {
                t[v].minimum = 1;
                t[v].zeros = 1;
            }
            
        }
        else {
            if (i < t[2 * v + 1].r) {
                inverse(2 * v + 1, i);
            }
            else {
                inverse(2 * v + 2, i);
            }
            update(v);
        }
    }
    void change(int v, int i, int val) {
        if (t[v].r - t[v].l == 1) {
            t[v].minimum = val;
            t[v].maxElem = val;
        }
        else {
            if (i < t[2 * v + 1].r) {
                change(2 * v + 1, i, val);
            }
            else {
                change(2 * v + 2, i, val);
            }
            update(v);
        }
    }
    int nth_zeros(int k) {
        return nth_zeros(0, k);
    }
    int nth_zeros(int v, int k) {
        if (t[v].r - t[v].l == 1) {
            return t[v].l;
        }
        else {
            if (t[2 * v + 1].zeros <= k) {
                return nth_zeros(2 * v + 2, k - t[2 * v + 1].zeros);
            }
            else {
                return nth_zeros(2 * v + 1, k);
            }
        }
    }
    int minIndexV(int x, int i) {
        return minIndexV(0, i, n, x);
    }
    int minIndexV(int v, int l, int r, int x) {
        if ((t[v].r - t[v].l == 1) && l <= t[v].l && t[v].r <= r) {
            if (t[v].maxElem < x) {
                return INT_MAX;
            }
            return t[v].l;
        }
        if (l <= t[v].l && t[v].r <= r) {
            if (t[v].maxElem < x) {
                return INT_MAX;
            }
            int left = minIndexV(2 * v + 1, l, r, x);
            int right = minIndexV(2 * v + 2, l, r, x);
            return left > right ? right : left;
        }
        else if (t[v].r <= l || t[v].l >= r) {
            return INT_MAX;
        }
        else {

            int left = minIndexV(2 * v + 1, l, r, x);
            int right = minIndexV(2 * v + 2, l, r, x);
            return left > right ? right : left;

        }
    }
    
};


int main()
{

    //vector<int> a = { 1, 1, 1, 1, 5, 1, 2, 3, 5 };
    //segment_tree st(a);
    //st.change(2, 0);
    //cout << st.min(1, 6).second;
    //cout << st.min(1, 6).first;
    int n, m;
    cin >> n >> m;
    vector<int> a;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    segment_tree st(a);
    for (int j = 0; j < m; j++) {
        int op, p, q;
        cin >> op >> p >> q;
        if (op == 1) {
            st.change(p, q);
        }
        else {
            int ans = st.minIndexV(p, q);
            if (ans == INT_MAX) cout << -1 << endl;
            else cout << ans << endl;
        }
    }

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
