import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private int N;
    private int[][] POPULATION_MAP;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] POPULATION_MAP = new int[N][N];

        for (int i = 0; i < N; i++) {
            POPULATION_MAP[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        System.out.println(new Main(N, POPULATION_MAP).solve());
    }

    public Main(int N, int[][] POPULATION_MAP) {
        this.N = N;
        this.POPULATION_MAP = POPULATION_MAP;
    }

    int[][] zoning(int x, int y, int d1, int d2) {
        int[][] zoneMap = new int[N][N];
        // ZONE 1
        for (int i = 0; i < d1; i++) {
            zoneMap[x + i][y - i] = 5;
        }

        for (int i = 0; i < x + d1; i++) {
            for (int j = 0; j <= y && zoneMap[i][j] == 0; j++) {
                zoneMap[i][j] = 1;
            }
        }

        // ZONE 3
        for (int i = 0; i < d2; i++) {
            zoneMap[x + d1 + i][y - d1 + i] = 5;
        }

        for (int i = N - 1; i >= x + d1; i--) {
            for (int j = 0; j < y - d1 + d2 && zoneMap[i][j] == 0; j++) {
                zoneMap[i][j] = 3;
            }
        }

        // ZONE 4
        for (int i = d1; i > 0; i--) {
            zoneMap[x + i + d2][y - i + d2] = 5;
        }

        for (int i = N - 1; i > x + d2; i--) {
            for (int j = N - 1; j >= y - d1 + d2 && zoneMap[i][j] == 0; j--) {
                zoneMap[i][j] = 4;
            }
        }

        // ZONE 2
        for (int i = d2; i > 0; i--) {
            zoneMap[x + i][y + i] = 5;
        }

        for (int i = 0; i <= x + d2; i++) {
            for (int j = N - 1; j > y && zoneMap[i][j] == 0; j--) {
                zoneMap[i][j] = 2;
            }
        }

        return zoneMap;
    }

    int calcScore(int[][] zoneMap) {
        int[] zoneScore = new int[5];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                zoneScore[zoneMap[i][j] % 5] += POPULATION_MAP[i][j];
            }
        }
        int maxScore = zoneScore[0];
        int minScore = zoneScore[0];
        for (int i = 1; i < 5; i++) {
            if (zoneScore[i] > maxScore) {
                maxScore = zoneScore[i];
            }
            if (zoneScore[i] < minScore) {
                minScore = zoneScore[i];
            }
        }
        return maxScore - minScore;
    }

    int solve() {
        Integer minScore = null;

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                for (int d1 = 0; d1 < N; d1++) {
                    for (int d2 = 0; d2 < N; d2++) {
                        if (x + d1 + d2 >= N) continue;
                        if (y - d1 < 0 || y + d2 >= N) continue;
                        int[][] zoneMap = zoning(x, y, d1, d2);
                        int score = calcScore(zoneMap);
                        if (minScore == null || score < minScore) minScore = score;
                    }
                }
            }
        }

        return minScore;
    }

}
