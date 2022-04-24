import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// word input 받기
		String word = sc.next();
		
		
		//alpha_lst 만들어주기
		int [] alpha_lst = new int[26];
		for(int i=0; i<26; i++) {
			alpha_lst[i]=0;
		}
				
		
//		97~122번 //charAt 은 word의 인덱스에 해당하는 글자를 아스키숫자로 변환
		for(int i=0; i < word.length(); i ++ ) {
			int idx = word.charAt(i);
			alpha_lst[idx-97] ++;				
		}
		
		
//		System.out.println(Arrays.toString(alpha_lst));
		
		
		
		for(int i=0; i<26; i++) {
			System.out.print(alpha_lst[i] + " ");
		}
		
		
	}	
//	}sc.close();
}