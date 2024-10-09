#include <stdio.h>
#define MAX_LEN 10

int main (void) {
  int n = 0, k = 0;

  int coin_len = 0;
  int coins[MAX_LEN] = { 0 };
  
  scanf("%d %d", &n, &k);

  for (int i = 0;i < n;i++) {
    int input;
    scanf("%d", &input);
    if (input > k) continue;
    coins[coin_len++] = input;
  }

  int cnt = 0;
  for (int i = coin_len - 1; i >= 0;i--) {
    int this_cnt = k / coins[i];
    cnt += this_cnt;
    k -= this_cnt * coins[i];
  }
  printf("%d\n", cnt);
  
  return 0;
}
