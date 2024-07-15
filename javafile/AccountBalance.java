




import java.util.Scanner;

public class AccountBalance{

	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);

		System.out.println("Type 1 to deposit 2 to withdraw or -1 to check balance: ");
		int userInput = scanner.nextInt();

		int balance = 0;

		while (userInput != -1){



			if (userInput == 1){

				System.out.println("Deposit amount: ");
				int deposit = scanner.nextInt();
				balance += deposit;
			}

			else if (userInput == 2){

				System.out.println("Withdrawal amount: ");
				int withdraw = scanner.nextInt();
				balance -= withdraw;
			}


			else System.out.println("Invalid input.");

	

			System.out.println("Type 1 to deposit 2 to withdraw or -1 to check balance: ");
			userInput = scanner.nextInt();

	}

System.out.println(balance);

	}
}