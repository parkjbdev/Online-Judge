#include <iostream>
#define MAX 20
using namespace std;

unsigned long long dp[MAX][4] = {0};

unsigned long long upow10(int n) {
    unsigned long long ret = 1;
    for (int i = 0; i < n; i++)
        ret *= 10;

    return ret;
}

unsigned long long solve(int len, int state) {
    if (state == 3) {
        dp[len][state] = upow10(len);
        return dp[len][state];
    }
    if (len == 0) return 0;

    if (dp[len][state] != 0) return dp[len][state];

    unsigned long long ret = 0;
    for (int i = 0; i <= 9; i++)
        ret += solve(len - 1, i == 6 ? state + 1 : 0);
    dp[len][state] = ret;

    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long N;
    cin >> N;

    int target_len = 3;

    while (true) {
        unsigned long long curr_digit_cnt =
                8 * solve(target_len - 1, 0) + solve(target_len - 1, 1);
        if (N <= curr_digit_cnt) break;

        N -= curr_digit_cnt;
        target_len++;
    }

    int curr_state = 0;
    for (int i = target_len; i >= 1; i--) {
        for (int d = (i == target_len ? 1 : 0); d <= 9; d++) {
            int next_state = (curr_state == 3)
                                 ? 3
                                 : (d == 6 ? curr_state + 1 : 0);
            unsigned long long available = solve(i - 1, next_state);

            if (N <= available) {
                cout << d;
                curr_state = next_state;
                break;
            } else N -= available;
        }
    }

    return 0;
}
