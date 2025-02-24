import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 0; t < 10; t++) {
            br.readLine();
            Deque<Integer> deque = new ArrayDeque<>();
            StringTokenizer st = new StringTokenizer(br.readLine());

            while (st.hasMoreTokens()) {
                deque.add(Integer.valueOf(st.nextToken()));
            }

            while (deque.peekLast() != 0) {
                for (int i = 1; i <= 5; i++) {
                    int pop = deque.pop();
                    if (pop - i <= 0) {
                        deque.add(0);
                        break;
                    } else deque.add(pop - i);
                }
            }

            StringBuffer sb = new StringBuffer("#").append(t + 1).append(" ");

            while (!deque.isEmpty())
                sb.append(deque.pop()).append(" ");

            System.out.println(sb);
        }
    }
}
