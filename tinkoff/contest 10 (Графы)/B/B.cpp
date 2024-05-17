// A.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>
#include <set>

using namespace std;


struct UFD {
	int N;
	vector<int> parents;
	vector<int> rank;

	UFD(int n) {
		n++;
		N = n;
		parents.resize(n);
		rank.resize(n);
		for (int i = 0; i < n; i++) {
			parents[i] = i;
			rank[i] = 1;
		}
	}
	int find(int x) {
		if (parents[x] != x) {
			return find(parents[x]);
		}
		return x;
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
		return w;
	}

	long long kraskal(set <pair<int, pair <int, int>>> setds) {
		long long ans = 0;
		while (!setds.empty()) {
			pair<int, pair <int, int>> tmp = *(setds.begin());
			setds.erase(setds.begin());
			ans += uni(tmp.second.first, tmp.second.second, tmp.first);
			//cout << tmp.first << " " << tmp.second.first << endl;
		}
		return ans;
	}
};

int main()
{
	int n, m;
	cin >> n >> m;
	UFD ufd(n);
	set <pair<int, pair <int, int>>> setds;

	int b, e, w;
	for (int i = 0; i < m; i++) {
		cin >> b >> e >> w;
		setds.insert(make_pair(w, make_pair(b, e)));
	}

	cout << ufd.kraskal(setds);
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
