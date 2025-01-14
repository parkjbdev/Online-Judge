import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int test_case = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < test_case; i++) {
            int[] numbers = Arrays.stream(sc.nextLine()
                                            .split(" "))
                                  .mapToInt(Integer::parseInt)
                                  .toArray();
            int answer = solve(numbers);
            System.out.println(answer);
        }
    }

    public static int solve(int[] numbers) {
        int max = Arrays.stream(numbers)
                        .max()
                        .getAsInt();

        int sum = Arrays.stream(numbers)
                        .sum();

        int base = (max / 7) * 7;
        int add = 7 - sum % 7;

        int answer = base + add;
        if (answer <= max) answer += 7;
        return answer;
    }
}
