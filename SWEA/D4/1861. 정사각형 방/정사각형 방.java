import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int t = 0; t < TC; t++) {
            int N = Integer.parseInt(br.readLine());
            int[][] MAP = new int[N][N];
            StringTokenizer st;
            Set<Point> toVisit = new HashSet<>();

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    MAP[i][j] = Integer.parseInt(st.nextToken());
                    toVisit.add(new Point(i, j));
                }
            }

            int startRoom = N * N + 1;
            int maxMove = 0;

            int[] DXs = {-1, 1, 0, 0};
            int[] DYs = {0, 0, -1, 1};

            while (!toVisit.isEmpty()) {
                Point point = toVisit.iterator().next();
                toVisit.remove(point);
                Deque<Point> queue = new ArrayDeque<>();
                queue.offer(point);
                boolean[][] visit = new boolean[N][N];
                visit[point.x][point.y] = true;

                int moveCnt = 0;
                int minRoom = MAP[point.x][point.y];

                while (!queue.isEmpty()) {
                    Point pop = queue.poll();
                    moveCnt += 1;
                    minRoom = Math.min(minRoom, MAP[pop.x][pop.y]);

                    for (int i = 0; i < 4; i++) {
                        int nx = pop.x + DXs[i];
                        int ny = pop.y + DYs[i];
                        if (0 > nx || nx >= N || 0 > ny || ny >= N) continue;
                        if (visit[nx][ny]) continue;
                        if (Math.abs(MAP[nx][ny] - MAP[pop.x][pop.y]) > 1) continue;

                        Point nP = new Point(nx, ny);
                        queue.offer(nP);
                        toVisit.remove(nP);
                        visit[nx][ny] = true;
                    }
                }

                if (moveCnt == maxMove && startRoom > minRoom)
                    startRoom = minRoom;

                if (moveCnt > maxMove) {
                    maxMove = moveCnt;
                    startRoom = minRoom;
                }
            }

            sb.append("#").append(t + 1).append(" ").append(startRoom).append(" ").append(maxMove).append("\n");
        }

        System.out.println(sb);
        br.close();
    }
}
