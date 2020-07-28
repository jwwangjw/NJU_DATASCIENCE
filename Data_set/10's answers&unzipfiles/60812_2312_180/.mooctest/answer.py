import java.util.Scanner;
 
public class Main{
     
    public static long getNums(int n) {
        assert n > 0;
        int mod = 1_000_000_007;
        long result = 1;
        //求逆元
        long[] inv = new long[n + 3];
        inv[1] = 1;
        for (int i = 2; i < n + 3; i++) {
            inv[i] = (mod - mod / i) * inv[mod % i] % mod;
        }
        // 卡特兰数
        for (int i = 0; i < n; i++) {
            result = 2 * (2 * i + 1) * inv[i + 2] % mod * result % mod;
        }
        return result;
    }
     
    public static void main(String[] args) {
        try(Scanner input = new Scanner(System.in)) {
            while (input.hasNext()) {
                int n = input.nextInt();
                System.out.println(getNums(n));
            }
        }
    }
}
