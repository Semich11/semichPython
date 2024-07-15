import java.util.Scanner;

public class Exercise1{
	public static void main(String[] args){

		Scanner input = new Scanner(System.in);

		int number1 = 0;
		int number2 = 0;

		boolean flag = true;

		while(flag){

 			System.out.println("Enter first integer: ");
			number1 = input.nextInt();

			if(number1 == 1) flag = false;
			else if(number1 == 2) flag = false;


 			System.out.println("Enter second integer: ");
			number2 = input.nextInt();

			if(number2 == 1) flag = false;
			else if(number2 == 2) flag = false;


		}

		int total = number1 + number2;


		System.out.printf("The sum of %d and %d is %d", number1, number2, total);

	}
}
