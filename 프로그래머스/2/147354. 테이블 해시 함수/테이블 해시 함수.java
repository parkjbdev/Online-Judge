import java.util.*;
class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        Arrays.sort(data, (a,b) -> b[0] - a[0]);
        Arrays.sort(data, (a,b) -> a[col-1] - b[col-1]);
        
        for (int i = row_begin - 1;i < row_end;i++) {
            answer = answer ^ S(i + 1, data[i]);
        }
        
        return answer;
    }
    
    private int S(int num, int[] row) {
        if (num == 0) return 0;
        
        int result = 0;
        for (int i = 0;i < row.length;i++) {
            result += row[i] % num;
        }
        
        return result;
    }
}


