class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
        // (b - a + 1) * (a + b) / 2 -> 등차수열 공식
        for(int i=Math.min(a,b);i<=Math.max(a,b);i++){
            answer += i;
        }
        
        return answer;
    }
}