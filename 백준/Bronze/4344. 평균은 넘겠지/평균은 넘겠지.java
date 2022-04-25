import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int [] arr;
		
		int testcase = sc.nextInt();
		for(int i=0; i<testcase; i++) {
			int N = sc.nextInt();
			arr = new int[N];
			
			double sum = 0;
			for(int j = 0; j<N; j++) {
				int val = sc.nextInt();
				arr[j] = val;
				sum += val;
			}
			double avg = sum/N;
			double cnt = 0;
			for(int k=0; k<N; k++) {
				if (arr[k]>avg) {
					cnt++;
				}
			}
			System.out.printf("%.3f%%\n", (cnt/N)*100);
			// printf() %.3f 소수점 셋째자리
			// printf 에서 % 를 출력하려면 %%로 적어주어야 한다. 
			
			
			
		}//한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
	}
}