class Solution {
    public double solution(int[] numbers) {
        int answer = 0;
        for(int i=0;i<numbers.length;i++){
            answer += numbers[i];
        }
        
        return answer/(float)numbers.length;
    }
}