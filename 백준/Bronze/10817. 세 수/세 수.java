import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A, B, C;
		A = sc.nextInt();
		B = sc.nextInt();
		C = sc.nextInt();
		
		
		
		int tmp = A;  //A와 B를 비교해서, 더 큰 값을 넣어줌 // 만일 같으면 그냥 A의 값을 가짐
		int small = A;
		if (A<B) {
			tmp = B;
			small = A;
		}
			
		else if(A>B) {
			tmp = A;
			small = B;
		}

		if (tmp<=C)
			System.out.println(tmp);
		else
			//tmp > C ? A
			if (small>=C)
				System.out.println(small);
			else
				System.out.println(C);
	
			

		
		
	}//sc.close();
	
}