// A.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>

using namespace std;


struct UFD {
	int N;
	vector<int> parents;
	vector<int> minimum;
	vector<int> maximum;
	vector<int> size;
	vector<int> rank;

	UFD(int n) {
		n++;
		N = n;
		parents.resize(n);
		minimum.resize(n);
		maximum.resize(n);
		size.resize(n);
		rank.resize(n);
		for (int i = 0; i < n; i++) {
			parents[i] = minimum[i] = maximum[i] = i;
			size[i] = rank[i] = 1;
		}
	}

	vector<int> get(int x) {
		if (parents[x] != x) {
			return get(parents[x]);
		}
		return { minimum[x], maximum[x], size[x] };
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
		minimum[pset] = min(minimum[xset], minimum[yset]);
		maximum[pset] = max(maximum[xset], maximum[yset]);
		size[pset] = size[xset] + size[yset];
	}
};

int main()
{
	int n, m;
	cin >> n >> m;
	UFD ufd(n);
	for (int i = 0; i < m; i++) {
		string word;
		cin >> word;
		//cout << word << endl;
		if (word == "union") {
			int x, y;
			cin >> x >> y;
			ufd.uni(x, y);
		}
		else {
			int x; cin >> x;
			vector<int> apchi(3);
			apchi = ufd.get(x);
			for (int j = 0; j < 3; j++) {
				cout << apchi[j] << " ";
			}
			cout << endl;
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
