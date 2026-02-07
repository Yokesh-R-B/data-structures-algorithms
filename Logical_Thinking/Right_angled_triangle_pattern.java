package Logical_Thinking;

import java.util.Scanner;

public class Right_angled_triangle_pattern{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        System.out.print("Input: N = ");
        int N = Integer.valueOf(scanner.nextLine());

        for (int i = 1; i <= N; i++){
            for(int j = 1; j <= i; j++){
                System.out.print("*");
            }

            System.out.println();
    }
    }
}