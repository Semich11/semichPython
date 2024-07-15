

public class Exercise10{
	public static void main(String[] args){		
	
	int principal = 1000;
	int annual_rate = 7/100;
	int number_of_years = 10;

	for(int year = 1; year <= 30; year++){
		int amount_on_deposit = principal * (1 + annual_rate)*year;
		System.out.printf("for year %d the amount on deposit is %d ", year, amount_on_deposit)

	}

	}
}
