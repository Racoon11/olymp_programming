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
    long long sum, add, set = -1;
};

struct segment_tree {

    vector<node> t;
    int n;

    segment_tree(const vector<long long>& a) {
        n = a.size();
        t.resize(4 * n);
        build(0, 0, n, a);
    }
    //void update(int v) {
      //  t[v].maxElem = min(t[2 * v + 1].maxElem, t[2 * v + 2].maxElem);

    //}
    void update(int v) {
        push(2 * v + 1);
        push(2 * v + 2);
        t[v].sum = t[2 * v + 1].sum + t[2 * v + 2].sum;
    }
    void build(int v, int l, int r, const vector<long long>& a) {
        t[v].l = l;
        t[v].r = r;

        if (r - l == 1) {
            t[v].sum = a[l];
        }
        else {
            int m = (l + r) / 2;

            build(2 * v + 1, l, m, a);
            build(2 * v + 2, m, r, a);


            update(v);
        }
    }

    void push_add(int child, long long x) {
        if (t[child].set == -1) {
            t[child].add += x;
        }
        else {
            t[child].set += x;
        }
    }

    void push_set(int child, long long x) {
        t[child].set = x;
        t[child].add = 0;
    }

    long long get_sum(long long v) {
        push(v);
        return t[v].sum;
    }

    void push(int v) {
        if (t[v].set != -1) {
            t[v].sum = (t[v].r - t[v].l) * t[v].set;
        }
        else {
            t[v].sum += (t[v].r - t[v].l) * t[v].add;
        }
        if (t[v].r - t[v].l > 1) {
            if (t[v].set != -1) {
                push_set(2 * v + 1, t[v].set);
                push_set(2 * v + 2, t[v].set);
            }
            else {
                push_add(2 * v + 1, t[v].add);
                push_add(2 * v + 2, t[v].add);
            }
        }
       
        t[v].set = -1;
        t[v].add = 0;
    }

    long long get(int l, int r) {
        return get(0, l, r);
    }
    long long get(int v, int l, int r) {
        push(v);
        if (l <= t[v].l && t[v].r <= r) {
            return t[v].sum;
        }
        else if (t[v].r <= l || t[v].l >= r) {
            return 0;
        }
        else {

            long long s1 = get(2 * v + 1, l, r);
            long long s2 = get(2 * v + 2, l, r);
            return s1 + s2;

        }
    }

    
    void add(int l, int r, int x) {
        add(0, l, r, x);
    }
    void add(int v, int l, int r, int x) {
        push(v);
        if (l <= t[v].l && t[v].r <= r) {
            push_add(v, x);
            push(v);
        }
        else if (t[v].r <= l || r <= t[v].l) {
            return;
        }
        else {
            add(2 * v + 1, l, r, x);
            add(2 * v + 2, l, r, x);
            t[v].sum += get_sum(2 * v + 1) + get_sum(2 * v + 2);
        }
    }

    void set(int l, int r, long long x) {
        set(0, l, r, x);
    }
    void set(int v, int l, int r, long long x) {
        //cout << v << endl;
        //cout << t[v].l << " " << t[v].r << endl;
        push(v);
        if (l <= t[v].l && t[v].r <= r) {
            push_set(v, x);
            push(v);
        }
        else if (t[v].r <= l || r <= t[v].l) {
            return;
        }
        else {
            set(2 * v + 1, l, r, x);
            set(2 * v + 2, l, r, x);
            t[v].sum += get_sum(2 * v + 1) + get_sum(2 * v + 2);
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
        int op, l, r;
        cin >> op >> l >> r;
        if (op == 1) {
            long long v;
            cin >> v;
            st.set(l, r, v);
        }
        else if (op == 2) {
            long long v;
            cin >> v;
            st.add(l, r, v);
        }
        else {
            cout << st.get(l, r) << endl;
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
