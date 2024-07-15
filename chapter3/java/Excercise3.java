import java.util.Scanner;

public class Exercise3{
	public static void main(String[] args){

		for(int row = 1; row <= 10; row ++){
		 	for(int colunm = 1; colunm <= 10; colunm++ ){
				if(row % 2 == 1) System.out.print("<");
				else System.out.print(">");
			}
		System.out.println(" ");
		}




	}
}
