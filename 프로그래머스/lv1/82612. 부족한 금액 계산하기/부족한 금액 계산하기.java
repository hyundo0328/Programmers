class Solution {
    public long solution(long price, long money, long count) {
//         long answer = 0;
//         for(int i=1;i<=count;i++) {
// 			answer += price*i;
// 		}
		
// 		if(answer>money) {
//             return answer-money;
// 		} else {
//             return 0;
// 		}
        long answer = Math.max(price * (count * (count + 1) / 2) - money, 0);
        return answer;
    }
}