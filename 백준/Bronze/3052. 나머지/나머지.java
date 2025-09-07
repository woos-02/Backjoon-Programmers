import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        boolean result;
        int[] arr = new int[10];
        int count = 0;
        
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt()%42;
        }
        
        for (int i = 0; i < arr.length; i++) {
            result = false;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    result=true;
                    break;
                }
            }
            if (result == false) {
                count++;
            }
        }
        System.out.println(count);
    }
}