#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int score;
    cin >> score;

    if (score == 100) cout << "A";
    else if (score < 60) cout << "F";
    else cout << static_cast<char>(9 - (score / 10) + 'A');

    return 0;
}