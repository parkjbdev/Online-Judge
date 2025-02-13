import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringBuffer sb = new StringBuffer();
            StringTokenizer st = new StringTokenizer(br.readLine());
            String answer = new Solution(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())).solve();

            sb.append("#").append(t).append(" ").append(answer);
            System.out.println(sb);
        }
    }

    int N, M;

    Solution(int N, int M) {
        this.N = N;
        this.M = M;
    }

    String solve() {
        return ((this.M & ((1 << this.N) - 1)) == ((1 << this.N) - 1)) ?
            "ON": "OFF";
    }
}