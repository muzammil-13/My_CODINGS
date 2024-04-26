import java.util.Scanner;
public class IfSample{
public static void main(String args[]){
	Scanner s=new Scanner(System.in);
	System.out.println("Enter a number:");
int num=s.nexInt();
if(num<0){
System.out.println("number is negative");
}else{
System.out.println("number is positive");
}
}
}