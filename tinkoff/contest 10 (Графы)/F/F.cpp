// E.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

class Graph
{
    int V;    // No. of vertices

    // In a weighted graph, we need to store vertex 
    // and weight pair for every edge
    list< pair<int, pair<long long, int>> >* adj;
    long long INF = 100'000'000;

public:
    Graph(int root) {
        V = root;
        adj = new list< pair<int, pair<long long, int>> >[V];
    }

    // function to add an edge to graph
    void addEdge(int u, int v, long long w, int t) {
        adj[u].push_back(make_pair(v, make_pair(w, t)));
        adj[v].push_back(make_pair(u, make_pair(w, t)));
    }

    // prints shortest path from s
    long long shortestPath(int s, int minWeight) {
        set <pair <int, int>> setds;
        vector<long long> dist(V, INF);

        setds.insert(make_pair(0, s));
        dist[s] = 0;
        while (!setds.empty()) {
            pair<int, int> tmp = *(setds.begin());
            setds.erase(setds.begin());

            int u = tmp.second;
            list < pair<int, pair<long long, int>> >::iterator i;
            for (i = adj[u].begin(); i != adj[u].end(); i++) {
                int v = (*i).first;
                long long weight = (*i).second.first;
                int time = (*i).second.second;

                if ((dist[v] > dist[u] + time) and weight >= minWeight) {
                    if (dist[v] != INF)
                        setds.erase(setds.find(make_pair(dist[v], v)));
                    dist[v] = dist[u] + time;
                    setds.insert(make_pair(dist[v], v));
                }
            }
        }
        return dist[V-1];
    }
    long long dijkstra(int s, int minWeight) {
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
            list < pair<int, pair<long long, int>> >::iterator i;
            for (i = adj[v].begin(); i != adj[v].end(); i++) {
                int u = (*i).first;
                long long weight = (*i).second.first;
                int time = (*i).second.second;
                if ((d[u] > d[v] + time) and weight >= minWeight)
                    d[u] = d[v] + time;
            }
        }
        return d[V-1];
    }
};



int main()
{
    const long long cupWeight = 100, maxTime = 1440, carWeight = 3'000'000;
    int n, m;
    cin >> n >> m;
    Graph g(n);
    int v1, v2, t;
    long long w, wChanged;
    
    for (int i = 0; i < m; i++) {
        cin >> v1 >> v2 >> t >> w;
        wChanged = (w - carWeight) / cupWeight;
        /*left = min(left, max((long long) 0, wChanged));
        right = max(right, wChanged);*/
        g.addEdge(v1 - 1, v2 - 1, wChanged, t);
    }
    
    long long mid, timeLoc;
    long long right = 10'000'000, left = 0;
    //right+=10;
    while (right - left > 1) {
        mid = (right + left) / 2;
        timeLoc = g.dijkstra(0, mid);
        if (timeLoc > maxTime) {
            right = mid - 1;
        }
        else left = mid;

    }
    //left = (right + left) / 2;
    //cout << right << " " << left << endl;
    timeLoc = g.dijkstra(0, left);
    int timeLoc2 = g.dijkstra(0, right);
    if (timeLoc > maxTime) cout << 0;
    else if (timeLoc2 <= maxTime) cout << right;
    else cout << left;
    
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
