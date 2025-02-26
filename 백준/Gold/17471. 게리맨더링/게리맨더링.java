import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {
    private int N;
    private int[] POPULATION;
    private List<Integer>[] GRAPH;
    private int POPULATION_SUM = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] POPULATION = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            POPULATION[i] = Integer.parseInt(st.nextToken());
        }

        List[] GRAPH = new List[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            st.nextToken(); // Ignore count
            GRAPH[i] = new ArrayList<>(st.countTokens());
            while (st.hasMoreTokens()) {
                GRAPH[i].add(Integer.parseInt(st.nextToken()) - 1);
            }
        }

        System.out.println(new Main(N, POPULATION, GRAPH).solve());
    }

    public Main(int N, int[] POPULATION, List<Integer>[] GRAPH) {
        this.N = N;
        this.POPULATION = POPULATION;
        this.GRAPH = GRAPH;
        for (int population : POPULATION) POPULATION_SUM += population;
    }

    private static int visit(int visit, int bit) {
        return visit | (1 << bit);
    }

    private static boolean isVisit(int visit, int bit) {
        return ((visit >> bit) & 0b1) == 1;
    }

    int calcScore(int startCity, int visitBit) {
        int sum = 0;

        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(startCity);
        visitBit = visit(visitBit, startCity);

        while (!queue.isEmpty()) {
            int pop = queue.poll();
            sum += POPULATION[pop];

            for (int nct : GRAPH[pop]) {
                if (isVisit(visitBit, nct)) continue;
                visitBit = visit(visitBit, nct);
                queue.offer(nct);
            }
        }

        if (visitBit != ((1 << N) - 1)) return -sum;
        return sum;
    }

    int solve() {
        int minScore = POPULATION_SUM;
        int combCnt = 1 << N;
        for (int visitBit = 2; visitBit < combCnt; visitBit += 2) {
            int s1 = calcScore(0, visitBit);
            if (s1 < 0) continue;

            int anotherVisitBit = (~visitBit) & ((1 << N) - 1);
            int anotherCity = (int) (Math.log(visitBit & -visitBit) / Math.log(2));

            int s2 = calcScore(anotherCity, anotherVisitBit);
            if (s2 < 0) continue;

            minScore = Math.min(minScore, Math.abs(s1 - s2));
        }

        if (minScore == POPULATION_SUM) minScore = -1;

        return minScore;
    }
}