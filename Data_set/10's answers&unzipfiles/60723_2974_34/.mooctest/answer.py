import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
 
public class Main {
	static int n;
	static String str = new String();
	static int max = 0;
	static int A, B, C;
    public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		n = in.nextInt();
		str = in.next();
		for (int t = 1; t < n-1; t++) {
			A = panduan(str.substring(0, t));
			B = quan(str.substring(t, n)) - panduan(str.substring(t, n));
			if (max < A*B) {
				max = A*B;
			}
		}
		System.out.println(max);
	}
    /**
     * B的要求是找出 不相同的非正回文子串 这里采用曲线救国的方案，求出B的 全部不相同子串 的个数，减去B中 不相同的正回文子串 的个数
     * 
     * */
	private static int quan(String sub) {
		// TODO Auto-generated method stub
		Set<String> set = new HashSet<String>();
		for (int i = 1; i <= sub.length(); i++) {
			for (int start = 0; start <= sub.length()-i; start++) {
				String s = sub.substring(start, start+i);
				set.add(s);
			}
		}
		return set.size();
	}
	/**
	 * 对于一个字符串，查找其中包含的正回文串个数
	 * */
	private static int panduan(String sub) {
		// TODO Auto-generated method stub
		Set<String> set = new HashSet<String>();
		set.clear();
		for (int i = 1; i <= sub.length(); i+=2) {
			for (int start = 0; start <= sub.length()-i; start++) {
				String s = sub.substring(start, start+i);
				if (huiwen(s) == true) {
					set.add(s);
				}
			}
		}
		return set.size();
	}
	/**
	 * 判断回文
	 * */
	private static boolean huiwen(String s) {
		// TODO Auto-generated method stub
		for (int i = 0; i < s.length()/2; i++) {
			if (s.charAt(i) == s.charAt(s.length()-1-i)) {
				continue;
			} else {
				return false;
			}
		}
		return true;
	}
}
