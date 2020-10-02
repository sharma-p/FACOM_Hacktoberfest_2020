package fundamentals;

import java.util.Scanner;

public class NumberStarPattern {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	   Scanner s = new Scanner (System.in);
		
			Scanner sc= new Scanner(System.in);
        int N = sc.nextInt();
        
        for(int i=1;i<N+1;i++)
        {
                     for(int j=0;j<N-i;j++)
                    {
                        System.out.print(N-j);
                    } 
            
                    System.out.print("*");
            
                    for(int k=i-1;k>0;k--)
                    {
                        System.out.print(k);
                    } 
            
            
        System.out.println("");
        }
	}

}
