import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int N, int number) {
        return new Prog42895(N, number).solve();
    }
}

class Prog42895 {
  public final int MAX_SPLIT = 8;
  public final int N;
  public final int number;
  public Set<Integer>[] sets = new Set[MAX_SPLIT];

  public Prog42895(int N, int number) {
    this.N = N;
    this.number = number;
  }

  public int solve() {
    int answer = -1;

    for (int nTimes = 1; nTimes <= MAX_SPLIT; nTimes++) {
      int setIdx = nTimes - 1;
      sets[setIdx] = new HashSet<>();
      for (int i = 0; i < nTimes; i++) {
        if (i == 0) {
          int repeated = Integer.parseInt(Integer.toString(N).repeat(nTimes));
          sets[setIdx].add(repeated);
        } else sets[setIdx].addAll(arithmeticAddSet(i - 1, nTimes - i - 1));
      }
      if (sets[setIdx].contains(number)) {
        answer = nTimes;
        break;
      }
    }
    
    return answer;
  }

  private Set<Integer> arithmeticAddSet(int idx1, int idx2) {
    Set<Integer> tmpSet = new HashSet<>();
    for (int value1 : sets[idx1]) {
      for (int value2 : sets[idx2]) {
        tmpSet.add(value1 + value2);
        tmpSet.add(value1 - value2);
        tmpSet.add(value1 * value2);
        if (value2 != 0)  tmpSet.add(value1 / value2);
      }
    }
    return tmpSet;
  }
}