import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int count = 0;
        int N = sc.nextInt();
        int[] arr = new int[N];
        int b = sc.nextInt();
        
        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        for(int j = 0; j < arr.length; j++){
            if(b > arr[j]){
                System.out.print(arr[j] + " ");
            }
        }
    }
}