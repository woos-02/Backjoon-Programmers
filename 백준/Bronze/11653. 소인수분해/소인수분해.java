import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        // n ==1 이면 아무것도 출력x
        if (n == 1){
            System.out.println();
        } else {
            for (int i = 2; i < 10000000; i++) {
                // 나누어진 n이 1이 되면 for문 빠져나감
                if (n == 1) break;
                if (n%i == 0) {
                    n = n/i;
                    System.out.println(i);
                    // i를 2로 초기화
                    i = 1;
                    continue;
                }
            }
        }
    }
}