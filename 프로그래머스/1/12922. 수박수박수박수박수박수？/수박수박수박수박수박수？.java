class Solution {
    public String solution(int n) {
        return "수박".repeat(n/2).concat(n%2==0?"":"수");
    }
}