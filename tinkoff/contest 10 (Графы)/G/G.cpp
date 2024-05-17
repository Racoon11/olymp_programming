// E.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <list>
#include <set>
#include <vector>

using namespace std;

class Graph
{
    int V;    // No. of vertices

    // In a weighted graph, we need to store vertex 
    // and weight pair for every edge
    list< pair<int, int> >* adj;
    const long long INF = 1'000'000'000'000;

public:
    Graph(int root) {
        V = root;
        adj = new list<pair<int, int> >[V];
    }

    // function to add an edge to graph
    void addEdge(int u, int v, int w) {
        adj[u].push_back(make_pair(v, w));
        adj[v].push_back(make_pair(u, w));
    }

    // prints shortest path from s
    long long dijkstra(int s, int s2) {
        vector<long long> d(V, INF), a(V, 0);
        d[s] = 0;
        for (int j = 0; j < V; j++) {
            // находим вершину с минимальным d[v] из ещё не помеченных
            int v = -1;
            for (int u = 0; u < V; u++)
                if (!a[u] && (v == -1 || d[u] < d[v]))
                    v = u;
            // помечаем её и проводим релаксации вдоль всех исходящих ребер
            a[v] = true;
            list < pair<int, int> >::iterator i;
            for (i = adj[v].begin(); i != adj[v].end(); i++) {
                int u = (*i).first;
                int time = (*i).second;
                if ((d[u] > d[v] + time))
                    d[u] = d[v] + time;
            }
        }
        return d[s2];
    }
    long long shortestPath(int s, int s2) {
        set <pair <int, int>> setds;
        vector<long long> dist(V, INF);

        setds.insert(make_pair(0, s));
        dist[s] = 0;
        while (!setds.empty()) {
            pair<int, int> tmp = *(setds.begin());
            setds.erase(setds.begin());

            int u = tmp.second;
            list < pair<int, int>>::iterator i;
            for (i = adj[u].begin(); i != adj[u].end(); i++) {
                int v = (*i).first;
                int weight = (*i).second;

                if (dist[v] > dist[u] + weight) {
                    if (dist[v] != INF)
                        setds.erase(setds.find(make_pair(dist[v], v)));
                    dist[v] = dist[u] + weight;
                    setds.insert(make_pair(dist[v], v));
                }
            }
        }
        return dist[s2];
    }
    long long d(int start, int end) {
        vector<long long> dist(V, INF);
        dist[start] = 0;
        set<pair<int, int> > unused;
        unused.insert(make_pair(0, start));
        while (!unused.empty())
        {
            int i = unused.begin()->second;
            unused.erase(unused.begin());
            for (auto edge : adj[i])
            {
                int j = edge.first;
                int wt = edge.second;
                if (dist[i] + wt < dist[j])
                {
                    unused.erase(make_pair(dist[j], j));
                    dist[j] = dist[i] + wt;
                    unused.insert(make_pair(dist[j], j));
                }
            }
        }
        return dist[end];
    }
};



int main()
{
    const long long INF = 1'000'000'000'000;
    int n, m;
    cin >> n >> m;
    Graph g(n);
    int v1, v2, w;
    for (int i = 0; i < m; i++) {
        cin >> v1 >> v2 >> w;
        g.addEdge(v1 - 1, v2 - 1, w);
    }

    int a, b, c;
    cin >> a >> b >> c;
    a--; b--; c--;
    long long w1 = g.d(a, b);
    long long w2 = g.d(a, c);
    long long w3 = g.d(b, c);
    long long p1 = w1 + w3;
    long long p2 = w2 + w3;
    long long p3 = w1 + w2;
    if (p1 > INF && p2 > INF && p3 > INF) cout << -1;
    else cout << min(p3, min(p1, p2));
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
