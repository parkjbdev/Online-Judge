#include <iostream>
#include <stack>
#include <deque>

using namespace std;

int main() {
    int N;
    cin >> N;

    deque<int> main_line(N);
    stack<int> temp_line;
    for (int i = 0; i < N; i++) cin >> main_line[i];

    int current = 1;

    while (current < N) {
        if (!main_line.empty() && main_line.front() == current) {
            main_line.pop_front();
            current++;
        } else if (!temp_line.empty() && temp_line.top() == current) {
            temp_line.pop();
            current++;
        } else {
            while (!main_line.empty()) {
                temp_line.push(main_line.front());
                main_line.pop_front();
                if (temp_line.top() == current) break;
            }
            if (main_line.empty() && temp_line.top() != current) {
                cout << "Sad";
                return 0;
            }
        }
    }

    cout << "Nice";
    return 0;
}
