import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test_case = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < test_case; i++) {
            String S = sc.nextLine();
            int K = sc.nextInt();
            sc.nextLine();
            int[] X = Arrays.stream(sc.nextLine()
                                      .split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

            String answer = solve(S, K, X);
            System.out.println(answer);
        }
    }

    public static String solve(String S, int K, int[] X) {
        long sum = Arrays.stream(X)
                         .asLongStream()
                         .sum();
        if (sum > 0) {
            sum %= S.length();
            return S.substring((int) sum) + S.substring(0, (int) sum);
        } else if (sum < 0) {
            sum += (-sum / S.length() + 1) * S.length();
            return S.substring((int) sum) + S.substring(0, (int) sum);
        } else {
            return S;
        }
    }
}