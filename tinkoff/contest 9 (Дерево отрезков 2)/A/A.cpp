// B.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <climits>
#include <limits>
using namespace std;

struct node {
    int l, r;
    long long minElem;
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

    void print() {
        for (int i=0; i < 4 * n; i++) {
            cout << t[i].minElem << " ";
        }
        cout << endl;

    }
    void update(int v) {
        up(2 * v + 1);
        up(2 * v + 2);
        t[v].minElem = min(t[2 * v + 1].minElem, t[2 * v + 2].minElem);

    }
    void build(int v, int l, int r, const vector<long long>& a) {
        t[v].l = l;
        t[v].r = r;

        if (r - l == 1) {
            t[v].minElem = a[l];
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
            t[v].minElem += t[v].promisAdd;
        }
        else {
            t[v].minElem += t[v].promisAdd;
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


    long long minElem(int l, int r) {
        return minElem(0, l, r);
    }
    long long minElem(int v, int l, int r) {
        up(v);

        if (l <= t[v].l && t[v].r <= r) {
            return t[v].minElem;
        }
        else if (t[v].r <= l || t[v].l >= r) {
            
            return LLONG_MAX;
        }
        else {
            long long lmin, rmin;

            lmin = minElem(2 * v + 1, l, r);
            rmin = minElem(2 * v + 2, l, r);

            return min(lmin, rmin);

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
    vector<long long> a;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        a[i] = 0;
    }
    segment_tree st(a);
    for (int j = 0; j < m; j++) {
        int op, p, q;
        cin >> op >> p >> q;
        if (op == 1) {
            long long v;
            cin >> v;
            st.add(p, q, v);
           /* for (int j = p; j < q; j++) {
                a[j] += v;
            }*/
        }
        else {
            long long ans = st.minElem(p, q);
            //st.print();
            cout << ans << endl;
            /*long long ans2 = -1;
            for (int j = p; j < q; j++) {
                if (ans2 == -1) ans2 = a[j];
                ans2 = min(ans2, a[j]);
            }
            cout << ans2 << endl;*/
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
