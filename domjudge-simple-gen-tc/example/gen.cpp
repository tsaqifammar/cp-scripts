#include <bits/stdc++.h>
using namespace std;

using ll = long long;

mt19937 rng(chrono::system_clock::now().time_since_epoch().count());
ll random(ll a, ll b) {
	if (a > b) return 0;
    return a + rng() % (b - a + 1);
}

int main() {
	int n = random(1, 10);
	cout << n << '\n';

	for (int i = 0; i < n; i++)
		cout << random(1, 100) << ' ';
}
