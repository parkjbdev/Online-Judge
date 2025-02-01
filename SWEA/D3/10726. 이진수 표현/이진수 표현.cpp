#include <iostream>

using namespace std;

int main(void) {
  int TC;
  cin >> TC;

  for (int T = 1; T <= TC; T++) {
    int N, M;
    cin >> N >> M;

    int bits = ((1 << N) - 1);

    if ((M & bits) == bits) {
      cout << "#" << T << " ON" << endl;
    } else {
      cout << "#" << T << " OFF" << endl;
    }
  }
}
