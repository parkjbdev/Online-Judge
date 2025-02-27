import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t <= TC; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int dPrice = Integer.parseInt(st.nextToken());
            int mPrice = Integer.parseInt(st.nextToken());
            int qPrice = Integer.parseInt(st.nextToken());
            int yPrice = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] plan = new int[12];
            for (int i = 0; i < 12; i++) {
                plan[i] = Integer.parseInt(st.nextToken());
            }

            int[] dp = new int[13];

            for (int month = 1; month <= 12; month++) {
                int dOption = dp[month - 1] + plan[month - 1] * dPrice;
                int mOption = dp[month - 1] + mPrice;
                int qOption = month >= 3 ? dp[month - 3] + qPrice : qPrice;
                int yOption = month == 12 ? yPrice : Integer.MAX_VALUE;

                dp[month] = Math.min(Math.min(dOption, mOption), Math.min(qOption, yOption));
            }

            sb.append("#").append(t).append(" ").append(dp[12]).append("\n");
        }

        System.out.print(sb);
    }
}
