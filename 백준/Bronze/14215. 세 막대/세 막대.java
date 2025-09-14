import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int max = a;
        int rem = b + c;
        if(b > max) {
            max = b;
            rem = a + c;
        }
        if(c > max) {
            max = c;
            rem = a + b;
        }

        if(max >= rem) {
            max = rem - 1;
        }

        System.out.println(max+rem);
    }
}