import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public static void main(String[] args) throws IOException {
        int tc = 10;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 1; t <= tc; t++) {
            int N = Integer.parseInt(br.readLine());
            List<Integer> cipher = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .boxed().collect(Collectors.toCollection(LinkedList::new));
            int commandCount = Integer.parseInt(br.readLine());
            Command[] commands = new Command[commandCount];

            int cnt = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());

            while (st.hasMoreTokens()) {
                String command = st.nextToken();
                if (command.equals("I")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    int[] s = new int[y];
                    for (int i = 0; i < y; i++)
                        s[i] = Integer.parseInt(st.nextToken());
                    commands[cnt++] = new Insertion(x, y, s);
                } else if (command.equals("D")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    commands[cnt++] = new Deletion(x, y);
                } else if (command.equals("A")) {
                    int y = Integer.parseInt(st.nextToken());
                    int[] s = new int[y];
                    for (int i = 0; i < y; i++)
                        s[i] = Integer.parseInt(st.nextToken());
                    commands[cnt++] = new Addition(y, s);
                }
            }

            StringBuffer sb = new StringBuffer("#" + t + " ");
            List<Integer> answer = new Solution(cipher, commands).solve().subList(0, 10);

            for (Integer crypto : answer) {
                sb.append(crypto).append(" ");
            }
            System.out.println(sb);
        }
    }

    interface Command {
        List<Integer> exec(List<Integer> cipher);
    }

    static class Insertion implements Command {
        int x, y;
        int[] s;

        Insertion(int x, int y, int[] s) {
            this.x = x;
            this.y = y;
            this.s = s;
        }

        @Override
        public List<Integer> exec(List<Integer> cipher) {
            for (int i = 0; i < y; i++) {
                cipher.add(x + i, s[i]);
            }
            return cipher;
        }
    }

    static class Deletion implements Command {
        int x, y;

        Deletion(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public List<Integer> exec(List<Integer> cipher) {
            for (int i = 0; i < y; i++) {
                cipher.remove(x);
            }
            return cipher;
        }
    }

    static class Addition implements Command {
        int y;
        int[] s;

        Addition(int y, int[] s) {
            this.y = y;
            this.s = s;
        }

        @Override
        public List<Integer> exec(List<Integer> cipher) {
            for (int i = 0; i < y; i++) {
                cipher.add(s[i]);
            }
            return cipher;
        }
    }

    List<Integer> cipher;
    Command[] commands;

    Solution(List<Integer> cipher, Command[] commands) {
        this.cipher = cipher;
        this.commands = commands;
    }

    List<Integer> solve() {
        for (Command command : commands) {
            cipher = command.exec(cipher);
        }
        return cipher;
    }
}
