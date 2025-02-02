import java.util.*;

class Solution {
  public int[] solution(int m, int n, int[][] picture) {
    return new Prob1829(m, n, picture).solve();
  }
}

class Prob1829 {
  private final int m, n;
  private final int[][] picture;
  private boolean[][] isVisit;
  public Prob1829(int m, int n, int[][] picture) {
    this.m = m;
    this.n = n;
    this.picture = picture;
    isVisit = new boolean[m][n];
  }

  public int[] solve() {
    int numberOfArea = 0;
    int maxSizeOfOneArea = 0;
    
    for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
        if(picture[i][j] != 0 && !isVisit[i][j]) {
          numberOfArea++;
          int result = dfs(i, j, picture[i][j]);
          if (result > maxSizeOfOneArea) maxSizeOfOneArea = result;
        }

    return new int[]{numberOfArea, maxSizeOfOneArea}; 
  }

  private boolean isRange(int m, int n) {
    return 0 <= m && m < this.m && 0 <= n && n < this.n;
  }

  private int dfs(int m, int n, int num) {
    if (!isRange(m, n)) return 0; 
    if (picture[m][n] != num) return 0;
    if (isVisit[m][n]) return 0;
    isVisit[m][n] = true;
    return 1 + dfs(m + 1, n, num) + dfs(m, n + 1, num) + dfs(m - 1, n, num) + dfs(m, n - 1, num);
  }
}