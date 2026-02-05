#include <iostream>
using namespace std;
#define MAX 21

int memo[MAX][MAX][MAX] = {0,};

int w(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) return 1;
    if (a > 20 || b > 20 || c > 20) return w(20, 20, 20);

    if (memo[a][b][c] != 0) return memo[a][b][c];

    if (a < b && b < c) {
        memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(
                            a, b - 1, c);
    } else {
        memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1)
                        -
                        w(a - 1, b - 1, c - 1);
    }

    return memo[a][b][c];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int a, b, c;
        cin >> a >> b >> c;
        int answer = w(a, b, c);
        if (a == -1 && b == -1 && c == -1) break;

        cout << "w(" << a << ", " << b << ", " << c << ") = " << answer << endl;
    }

    return 0;
}
