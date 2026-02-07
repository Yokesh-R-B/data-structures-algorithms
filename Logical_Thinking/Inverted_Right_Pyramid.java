package Logical_Thinking;

import java.util.Scanner;

public class Inverted_Right_Pyramid {
        public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input N = ");

        int N = Integer.valueOf(scanner.nextLine());

        for (int i = N; i>=1; i--){
            for(int j = i; j>=1; j--){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
