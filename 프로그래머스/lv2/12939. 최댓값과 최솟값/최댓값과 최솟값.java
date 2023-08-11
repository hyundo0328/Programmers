import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

class Solution {
    public String solution(String s) {
        StringTokenizer st = new StringTokenizer(s);
		LinkedList<Integer> arr = new LinkedList();

		while(st.hasMoreTokens()) {
			arr.add(Integer.parseInt(st.nextToken()));	
		}
		
		Collections.sort(arr);
		
        String answer = arr.peekFirst().toString()+" "+arr.peekLast();
        return answer;
    }
}