import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N, M, k, i, j, x, y;
		int [][] arr;
		
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N+1][M+1];
		for (int a=0; a<N; a++) {
			for (int b=0; b<M; b++) {
				int num = sc.nextInt();
				arr[a][b] = num;
			}
			
		}
		k = sc.nextInt();
		for(int c = 0; c<k; c++) {
			i = sc.nextInt();
			j = sc.nextInt();
			x = sc.nextInt();
			y = sc.nextInt();
			
			int s = 0;
			for(int d=i-1; d<x; d++) {
				for(int e=j-1; e<y; e++) {
					s += arr[d][e];
				}
			}System.out.println(s);
			
			
		}
		
		
		
		
	}//sc.close();
	
}
