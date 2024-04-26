import java.util.Scanner;

public class IfCondition {
	public static void main(String ar[]) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a number:");
		
		int num=sc.nextInt();
		
		if(num<0) {
			System.out.println("Negative Number");
		}else {
			System.out.println("Postive Number");
		}
		
		sc.close();
	}
}
