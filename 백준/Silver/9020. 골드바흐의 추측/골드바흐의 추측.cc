#include <iostream>

using namespace std;

bool is_factor(int n) {
  for (int i = 2;i * i <= n;i++) {
    if (n % i == 0) return false;
  }

  return true;
}

int main (void) {
  int T;
  cin >> T;

  for (int i = 0;i < T;i++) {
    int N;
    cin >> N;

    for (int part = N / 2; part > 0;part--) {
      int left = N - part;

      if (is_factor(left) && is_factor(part)){
        cout << part << " " << left << endl;
        break;
      } 
    }
  }

  return 0;
}
