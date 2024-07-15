

public class Exercise9{
	public static void main(String[] args){		
	
	int number = 81567;

	while( number > 0){
	int first = number % 10;
	System.out.println(first);
	number /= 10;
	}

	}
}
