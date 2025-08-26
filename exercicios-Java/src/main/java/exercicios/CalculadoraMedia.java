package exercicios;

import java.util.Scanner;
public class CalculadoraMedia {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double nota1 = sc.nextInt();
        double nota2 = sc.nextInt();
        double media = (nota1+nota2)/2;
        if(media<7.0){
            System.out.println("reprovado");
        } else{
            System.out.println("aprovado");
        }
        sc.close();
    }

}
