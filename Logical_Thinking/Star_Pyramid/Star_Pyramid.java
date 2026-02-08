package Logical_Thinking.Star_Pyramid;
import java.util.Scanner;

public class Star_Pyramid {
    public static void main(String[] args) {
        

        Scanner scanner = new Scanner(System.in);
        System.out.print("Input Format: N = ");
        int N = Integer.valueOf(scanner.nextLine());

        PrintHelp print = new PrintHelp();
        int count =0;
        for(int i = N; i>=1; i--){
            for(int j = i-1 ; j>=1;j--){
                print.blank();
            }
            for(int k = 0; k<(2*count+1);k++){
                print.star();
            }
            System.out.println();
            count++;
        }
        

    }
}
