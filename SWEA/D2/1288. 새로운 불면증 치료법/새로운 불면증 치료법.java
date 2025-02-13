import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 1; t <= tc; t++) {
            int answer = new Solution(Integer.parseInt(br.readLine())).solve();
            StringBuffer sb = new StringBuffer();

            sb.append("#").append(t).append(" ").append(answer);

            System.out.println(sb);
        }
    }

    int N;
    private boolean[] numberSeen;
    private int numberSeenCnt = 0;

    Solution(int N) {
        this.N = N;
        this.numberSeen = new boolean[10];
        this.numberSeenCnt = 0;
    }


    int solve() {
        int mult = 1;
        while (numberSeenCnt < 10) {
            String str = "" + N * (mult++);
            for (int i = 0; i < str.length(); i++) {
                if (!numberSeen[str.charAt(i) - '0']) {
                    numberSeenCnt++;
                    numberSeen[str.charAt(i) - '0'] = true;
                }
            }
        }

        return (mult - 1) * this.N;
    }
}