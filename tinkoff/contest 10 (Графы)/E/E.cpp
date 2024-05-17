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
    long long INF = 100'000'000;

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
    void shortestPath(int s) {
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
        for (int i = 0; i < V; i++) {
            cout << dist[i] << ' ';
        }
    }
};



int main()
{
    int n, m;
    cin >> n >> m;
    Graph g(n);
    int v1, v2, w;
    for (int i = 0; i < m; i++) {
        cin >> v1 >> v2 >> w;
        g.addEdge(v1 - 1, v2 - 1, w);
    }

    g.shortestPath(0);
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
