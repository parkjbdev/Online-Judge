import java.awt.*;
import java.io.*;
import java.util.*;
import java.util.List;

class Tokenizer extends StringTokenizer {

    public Tokenizer(String str, String delim, boolean returnDelims) {
        super(str, delim, returnDelims);
    }

    public Tokenizer(String str, String delim) {
        super(str, delim);
    }

    public Tokenizer(String str) {
        super(str);
    }

    public int nextInt() {
        return Integer.parseInt(nextToken());
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Tokenizer tok = new Tokenizer(br.readLine());

        int N = tok.nextInt();
        int L = tok.nextInt();
        int R = tok.nextInt();

        int[][] MAP = new int[N][N];

        for (int i = 0; i < N; i++) {
            tok = new Tokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int population = tok.nextInt();
                MAP[i][j] = population;
            }
        }
        int answer = 0;

        int[] DXs = {-1, 1, 0, 0};
        int[] DYs = {0, 0, -1, 1};

        List<Set<Point>> allies = new ArrayList<>();

        while (allies.size() != N * N) {
            allies = new ArrayList<>();
            boolean[][] visit = new boolean[N][N];

            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    if (visit[x][y]) continue;
                    Set<Point> allySet = new HashSet<>();
                    Deque<Point> queue = new ArrayDeque<>();
                    queue.offer(new Point(x, y));
                    while (!queue.isEmpty()) {
                        Point pop = queue.poll();
                        allySet.add(pop);

                        int xx = pop.x;
                        int yy = pop.y;

                        for (int i = 0; i < 4; i++) {
                            int dx = DXs[i];
                            int dy = DYs[i];
                            int nx = xx + dx;
                            int ny = yy + dy;

                            if (!(0 <= nx && nx < N && 0 <= ny && ny < N)) continue;
                            if (visit[nx][ny]) continue;

                            int diff = Math.abs(MAP[xx][yy] - MAP[nx][ny]);
                            if (diff >= L && diff <= R) {
                                queue.offer(new Point(nx, ny));
                                visit[nx][ny] = true;
                            }
                        }
                    }

                    allies.add(allySet);
                }
            }

            if (allies.size() != N * N) answer++;

            for (Set<Point> allySet : allies) {
                if (allySet.size() == 1) continue;

                int sum = 0;
                for (Point point : allySet) {
                    sum += MAP[point.x][point.y];
                }
                for (Point point : allySet) {
                    MAP[point.x][point.y] = sum / allySet.size();
                }
            }
        }

        System.out.println(answer);
    }
}
