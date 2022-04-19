import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int K, num, tmp, sum;
		
		
		
		
		K = sc.nextInt();
		ArrayList<Integer> numlist  = new ArrayList<>();  // arraylist객체생성
		
		tmp = 0;
		for(int k=0; k<K; k++) {
			num = sc.nextInt();
			if (num==0) {
				int len = numlist.size() -1;
				numlist.remove(len); //remove(idx)
			}
			else {
				numlist.add(num); //add(원소)
			}
		}
		
		sum = 0;
		for(int i=0; i<numlist.size(); i++) {  //arraylist의 크기 반환(size)
			sum += numlist.get(i);  //get(idx)
		}
		
		System.out.println(sum);
		
	}
}