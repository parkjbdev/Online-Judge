import java.util.*;

public class Solution {
  public int solution(int n, int[][] edge) {
    return new Prob49189_BFS(n, edge).solve();
  }
}

class Prob49189_BFS {
  public final int N;
  public final ArrayList<Integer>[] adjacentList;
  boolean[] isVisit;
  private final Queue<Integer> queue = new LinkedList<>();
  private int[] minDistance;

  public Prob49189_BFS(int n, int[][] edge) {
    this.N = n;
    adjacentList = new ArrayList[n];
    isVisit = new boolean[N];
    minDistance = new int[N];

    for (int i = 0; i < n; i++) adjacentList[i] = new ArrayList<>();

    for (int[] node : edge) {
      adjacentList[node[0] - 1].add(node[1] - 1);
      adjacentList[node[1] - 1].add(node[0] - 1);
    }
  }

  public int solve() {
    bfs(0);
    OptionalInt tmpMax = Arrays.stream(minDistance).max();
    int max = tmpMax.isPresent() ? tmpMax.getAsInt() : 0;
    return (int) Arrays.stream(minDistance).filter(a -> a == max).count();
  }

  private void bfs(int start) {
    int cntVisit = 0;
    Queue<Integer> levelQueue = new LinkedList<>();
    levelQueue.offer(0);

    visit(start);
    while (!queue.isEmpty()) {
      if (cntVisit >= N) break;

      int currentIdx = queue.poll();
      int level = levelQueue.poll();
      minDistance[currentIdx] = level;

      for (int nextIdx : adjacentList[currentIdx])
        if (!isVisit[nextIdx]) {
          levelQueue.offer(level + 1);
          cntVisit++;
          visit(nextIdx);
        }
    }
  }

  private void visit(int idx) {
    queue.offer(idx);
    isVisit[idx] = true;
  }
}