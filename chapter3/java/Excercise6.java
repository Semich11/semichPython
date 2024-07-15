import java.util.Scanner;

public class Exercise6{
	public static void main(String[] args){

		Scanner input = new Scanner(System.in);

		System.out.println("Have you had this problem before (Yes or no)?: ");

		String userInput = input.next();

		if (userInput.equalsIgnoreCase("yes")) System.out.print("Well, you have it again");
		else if (userInput.equalsIgnoreCase("no")) System.out.print("Well, you have it now");


	}
}
