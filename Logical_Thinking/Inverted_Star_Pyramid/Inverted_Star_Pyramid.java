package Logical_Thinking.Inverted_Star_Pyramid;

import java.util.Scanner;

import Logical_Thinking.Star_Pyramid.PrintHelp;

public class Inverted_Star_Pyramid {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input Format: N = ");
        int N = Integer.valueOf(scanner.nextLine());

        PrintHelp print = new PrintHelp();
        int count =0;
        for(int i = N-1; i>=0; i--){

            for(int j = 0 ; j<count;j++){
                print.blank();
            }

            for(int k = (2*i+1); k>0;k--){
                print.star();
            }

            System.out.println();
            count++;
        }
    }
}
