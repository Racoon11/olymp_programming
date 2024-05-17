// B.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

struct ans {
	int deep;
	int maxi;
	int mini;
};

ans check_tree(int tree[][2], int n) {
	if ((tree[n][0] == -1) and (tree[n][1] == -1)) {
		ans ret; ret.deep = 0; ret.maxi = n; ret.mini = n;
		return { 0, n, n };
	}
	int deep = 0;
	int maxi = n;
	int miniLeft = n;
	if (tree[n][0] != -1) {
		int left = tree[n][0];
		ans st = check_tree(tree, left);
		deep = st.deep; maxi = st.maxi;
		miniLeft = st.mini;
		if (maxi >= n) {
			return { -1, -1, -1 };
		}
	}
	maxi = max(n, maxi);
	int deep2 = 0;
	int mini = n;
	int maxiRight = n;
	if (tree[n][1] != -1) {
		int right = tree[n][1];
		ans st = check_tree(tree, right);
		deep2 = st.deep; mini = st.mini;
		maxiRight = st.maxi;
		if (mini <= n) {
			return { -1, -1, -1 };
		}
	}
	mini = min(n, mini);
	if ((deep != -1) and (deep2 != -1) and (abs(deep - deep2) <= 1)) {
		return { max(deep, deep2) + 1, maxiRight, mini };
	}
	return { -1, -1, -1 };
}


int main()
{
	int n, k;
	cin >> n >> k;
	int tree[100001][2];
	for (int i = 0; i < n; i++) {
		cin >> tree[i][0] >> tree[i][1];
	}

	ans ans1 = check_tree(tree, k);
	if (ans1.deep == -1) {
		cout << 0;
	}
	else {
		cout << 1;
	}
}
