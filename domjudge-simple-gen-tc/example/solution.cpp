#include <bits/stdc++.h>
using namespace std;

/*

Given a sequence a1, a2, ..., an. Sort it non-decreasingly.

*/
 
int main() {
    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr, arr + n);

    for (int i = 0; i < n; i++)
        cout << arr[i] << " \n"[i == n-1];
}

