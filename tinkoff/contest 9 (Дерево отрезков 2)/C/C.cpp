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
    int number, length;
    int left, right;
    int up = -1;
};

struct segment_tree {

    vector<node> t;
    int n;

    segment_tree(const vector<int>& a) {
        n = a.size();
        t.resize(4 * n);
        build(0, 0, n, a);
    }

    void print() {
        for (int i = 0; i < 4 * n; i++) {
            cout << t[i].number << "," << t[i].length << " ";
        }
        cout << endl;

    }
    void update(int v) {
        up(2 * v + 1);
        up(2 * v + 2);
        t[v].length = t[2 * v + 1].length + t[2 * v + 2].length;
        t[v].number = t[2 * v + 1].number + t[2 * v + 2].number;
        if (t[2 * v + 1].right && t[2 * v + 2].left) {
            t[v].number--;
        }
        t[v].left = t[2 * v + 1].left;
        t[v].right = t[2 * v + 2].right;

 
    }
    void build(int v, int l, int r, const vector<int>& a) {
        t[v].l = l;
        t[v].r = r;
        t[v].up = -1;

        if (r - l == 1) {
            t[v].length = a[l];
            t[v].number = a[l];
            t[v].left = t[v].right = a[l];
        }
        else {
            int m = (l + r) / 2;

            build(2 * v + 1, l, m, a);
            build(2 * v + 2, m, r, a);

            update(v);
        }
    }

    void add(int l, int r, int val) {
        add(0, l, r, val);
    }

    void up(int v) {
        if (t[v].up == -1) return;

        t[v].right = t[v].left = t[v].up;
        t[v].length = t[v].up ? t[v].r - t[v].l : 0;
        t[v].number = t[v].up ? 1 : 0;
        if (t[v].r - t[v].l == 1) {
            ;
        }
        else {

            t[2 * v + 1].up = t[v].up;
            t[2 * v + 2].up = t[v].up;
        }
        t[v].up = -1;
    }

    void add(int v, int l, int r, int val) {
        up(v);
        if (l <= t[v].l && t[v].r <= r) {
            t[v].up = val;
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
        //cout << "add: " << v << " " << t[v].number << " " << t[v].length << endl;
     }

};


int main()
{

    //vector<int> a = { 1, 1, 1, 1, 5, 1, 2, 3, 5 };
    //segment_tree st(a);
    //st.change(2, 0);
    //cout << st.min(1, 6).second;
    //cout << st.min(1, 6).first;
    int n;
    cin >> n;
    const int N = 1'000'000;
    vector<int> a;
    a.resize(N);
    for (int i = 0; i < N; i++) {
        a[i] = 0;
    }
    segment_tree st(a);

    int x, l;
    char c;
    for (int i = 0; i < n; i++) {
        cin >> c >> x >> l;
        x += 500'000;
        if (c == 'W') {
            st.add(x, x + l, 0);
        }
        else st.add(x, x + l, 1);
        cout << st.t[0].number << " " << st.t[0].length << endl;
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
