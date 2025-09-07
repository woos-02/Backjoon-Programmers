import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc =new Scanner(System.in);
		int total = sc.nextInt();
		int type = sc.nextInt();
        int rcp = 0;
		for(int i = 1; i <= type; i++) {
			int price = sc.nextInt();
            int cnt = sc.nextInt();
            rcp += price * cnt;
		}
        if (rcp == total) System.out.println("Yes");
        else System.out.println("No");
	}
}