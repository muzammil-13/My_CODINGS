import java.util.Scanner;

public class SampleInput{
	public static void main(String ar[]) {
		Scanner s =new Scanner(System.in);
		System.out.println("Enter 2 numbers:");
		
		int a=s.nextInt();
		int b=s.nextInt();
		
		System.out.println(a+"  "+b);
		
		s.close();
	}
}