// A.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>
#include <set>
using namespace std;


struct UFD {
	int N;
	vector<int> parents;
	vector<int> size;
	vector<int> rank;

	UFD(int n) {
		n++;
		N = n;
		parents.resize(n);
		size.resize(n);
		rank.resize(n);
		for (int i = 0; i < n; i++) {
			parents[i] = i;
			size[i] = rank[i] = 1;
		}
	}

	int find(int x) {
		if (parents[x] != x) {
			return find(parents[x]);
		}
		return x;
	}
	void uni(int x, int y) {
		int xset = find(x);
		int yset = find(y);
		if (xset == yset) return;

		if (rank[xset] < rank[yset]) {
			parents[xset] = yset;
		}
		else if (rank[yset] < rank[xset]) {
			parents[yset] = xset;
		}
		else {
			parents[yset] = xset;
			rank[xset]++;
		}
		int pset = find(x);

		size[pset] = size[xset] + size[yset];
	}

	long long uni(int x, int y, long long w) {
		int xset = find(x);
		int yset = find(y);
		if (xset == yset) return 0;

		//parents[xset] = yset;

		if (rank[xset] < rank[yset]) {
			parents[xset] = yset;
		}
		else if (rank[yset] < rank[xset]) {
			parents[yset] = xset;
		}
		else {
			parents[yset] = xset;
			rank[xset]++;
		}

		int pset = find(x);
		size[pset] = size[xset] + size[yset];
		return w;
	}

};

int main()
{
	int n, m;
	cin >> n >> m;
	UFD ufd((n+1) * (m+1));
	
	int k, v;
	set <pair<int, pair <int, int>>> edges;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> k;
			v = i * m + j;
			if (k == 1) {
				ufd.uni(v, (i + 1) * m + j);
			}
			else if (k == 2) {
				ufd.uni(v, i * m + j + 1);
			}
			else if (k == 3) {
				ufd.uni(v, (i + 1) * m + j);
				ufd.uni(v, i * m + j + 1);
			}
			if (i != (n-1)) edges.insert(make_pair(1, 
				make_pair(v, (i + 1) * m + j)));
			if (j != (m - 1)) edges.insert(make_pair(2,
				make_pair(v, i * m + j + 1)));
		}
	}
	int ans = 0;
	int len = 0;
	int loc;
	vector <pair<int, pair <int, int>>> ans2;
	while (!edges.empty()) {
		pair<int, pair <int, int>> tmp = *(edges.begin());
		edges.erase(edges.begin());
		loc = ufd.uni(tmp.second.first, tmp.second.second, tmp.first);
		if (loc != 0) {
			ans2.push_back(tmp);
			len++;
		}
		ans += loc;
		//cout << tmp.first << " " << tmp.second.first << endl;
	}
	cout << len << " " << ans << endl;
	int v1, v2;
	int i, j;
	while (!ans2.empty()) {
		pair<int, pair <int, int>> tmp = *(ans2.begin());
		ans2.erase(ans2.begin());
		v1 = tmp.second.first;
		i = v1 / m;
		j = v1 % m;
		cout << i + 1 << " "
			<< j + 1 << " "
			<< tmp.first << endl;
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
