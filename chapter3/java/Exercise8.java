import java.util.Scanner;
import java.util.Arrays;

public class Exercise8{
	public static void main(String[] args){		

	int[] numbers = new int[4];

 	int sum = 0;
	int product = 1;

	for(int count = 0; count < 4; count++){
		Scanner input = new Scanner(System.in);
		System.out.println("Enter first number");
		numbers[count] = input.nextInt();
 		sum += numbers[count];
		product += numbers[count];
	}

	System.out.println(Arrays.toString(numbers));

	int size = numbers.length;

	for(int count = 0; count < size; count++){
		for(int row = 0; row < size; row++){
			if(numbers[count] > numbers[row]){
				int temp = numbers[count];
				numbers[count] = numbers[row];
				numbers[row] = temp;
			}
		}
	}

	System.out.printf("Largest: %d%n", numbers[0]);
	System.out.printf("Smallest: %d%n", numbers[size - 1]);
	System.out.printf("Product: %d%n", product);
	System.out.printf("Sum: %d%n", sum);
	System.out.printf("Product: %d%n", sum / size);








	}
}
