import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        List<Integer>[] EDGES = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            EDGES[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            EDGES[s - 1].add(v - 1);
            EDGES[v - 1].add(s - 1);

            Collections.sort(EDGES[s - 1]);
            Collections.sort(EDGES[v - 1]);
        }

        new DFS(N, EDGES).recursive(V - 1);
        System.out.println();
        bfs(N, V, EDGES);
    }

    static class DFS {
        List<Integer>[] EDGES;
        boolean[] visit;

        DFS(int N, List<Integer>[] EDGES) {
            this.visit = new boolean[N];
            this.EDGES = EDGES;
        }

        public void recursive(int V) {
            if (!visit[V]) {
                System.out.print((V + 1) + " ");
                visit[V] = true;
            }
            for (int i = 0; i < EDGES[V].size();i++) {
                if (!visit[EDGES[V].get(i)]) recursive(EDGES[V].get(i));
            }
        }
    }

    public static void bfs(int N, int V, List<Integer>[] EDGES) {
        StringBuffer sb = new StringBuffer();

        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(V - 1);

        boolean[] visit = new boolean[N];
        visit[V - 1] = true;

        while (!queue.isEmpty()) {
            Integer pop = queue.poll();
            sb.append(pop + 1).append(" ");

            for (int i = 0; i < EDGES[pop].size(); i++) {
                int idx = EDGES[pop].get(i);
                if (!visit[idx]) {
                    visit[idx] = true;
                    queue.offer(idx);
                }
            }
        }

        System.out.println(sb);
    }
}