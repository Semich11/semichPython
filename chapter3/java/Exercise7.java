public class Exercise7{
	public static void main(String[] args){


		System.out.printf("%6s %6s %6s%n", "number","square", "cube");

		for(int number = 1; number <= 5; number++){
 			int square = number * number;
			int cube = number * number * number;
			System.out.printf("%6s %6s %6s%n", number,square,cube);

		}


	}
}
