package exercicios;

import java.util.Scanner;

public class Maioridade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();
        int idade = sc.nextInt();
        if(idade<18){
            System.out.println("menor de idade");
        } else {
            System.out.println("maior de idade");
        }
        sc.close();
    }
}
