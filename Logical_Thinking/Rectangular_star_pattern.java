package Logical_Thinking;
import java.util.Scanner;

public class Rectangular_star_pattern {

    public static void main(String[] args){

    Scanner scanner = new Scanner(System.in);
    System.out.print("Input: N = ");
    int N = Integer.valueOf(scanner.nextLine());

    for (int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            System.out.print("*");
        }
        System.out.println();
    }


    }
}
