#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 0;t < T;t++) {
        int M;
        cin >> M;

        priority_queue<int> maxq;
        priority_queue<int, vector<int>, greater<>> minq;

        cout << (M / 2 + 1) << "\n";

        for (int i = 0;i < M;i++) {
            int input;
            cin >> input;

            if (minq.empty() || input >= minq.top()) minq.push(input);
            else maxq.push(input);

            if (i % 2 == 1 && maxq.size() != minq.size()) {
                maxq.push(minq.top());
                minq.pop();
            }
            else if (i % 2 == 0 && maxq.size() > minq.size()) {
                minq.push(maxq.top());
                maxq.pop();
            }

            if (i % 2 == 0) cout << minq.top() << " ";
            if (i % 20 == 18) cout << "\n";
        }
        cout << "\n";
    }

    return 0;
}