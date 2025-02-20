import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 0; t < 10; t++) {
            int len = Integer.parseInt(br.readLine());
            char[] input = br.readLine().toCharArray();

            Stack<Character> stack = new Stack<>();

            for (int i = 0; i < len; i++) {
                char letter = input[i];
                if (i == 0) {
                    stack.push(letter);
                    continue;
                }

                stack.push(letter);

                while (stack.size() >= 2) {
                    char let1 = stack.pop();
                    char let2 = stack.pop();

                    if (let1 == ')' && let2 == '(' ||
                            let1 == ']' && let2 == '[' ||
                            let1 == '>' && let2 == '<' ||
                            let1 == '}' && let2 == '{') continue;

                    else {
                        stack.push(let2);
                        stack.push(let1);
                        break;
                    }
                }

            }
            StringBuffer sb = new StringBuffer("#").append(t + 1).append(" ");
            sb.append(!stack.isEmpty() ? 0 : 1);
            System.out.println(sb);
        }
    }
}