import java.util.Scanner;
 
public class Main{
 
    /**
     * @param args
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
 
        while (sc.hasNext()) {
            String re = sc.next();
            String er = sc.next();
            min = 100000;
            f(re, er, 0, 0);// 这是re > er 的情况
            System.out.println(min);
        }
    }
 
    public static int min;
 
    private static void f(String re, String er, int begin, int change) {
        if (change >= min) {
            return;// 本次递归的操作数都大于全局最小，此方法一定不是最优解
        }
 
        if (begin == re.length()) {
            if (er.length() > re.length()) {// 如果修改后的字符串er长度大于re 之后需要移除操作
                change += er.length() - re.length();
            }
 
            if (change < min) {
                min = change;
            }
            return;
        }
 
        if (begin == er.length()) {
            // 只能插入 因为错误的字符串长度不够
            // // 插入
            er = AddCharIndexOf(er, begin, re.charAt(begin));
            f(re, er, begin + 1, change + 1);
            //System.out.println("[长度不够]插入之后：" + er);
        } else {
            if (er.charAt(begin) != re.charAt(begin)) {
                String tmp = er;// 下面也需要递归 所以用变量先储存下来
                // 删除
                er = RemoveCharIndexOf(er, begin);
                f(re, er, begin, change + 1);
                //System.out.println("删除之后：" + er);
                er = tmp;// 回溯
 
                // // 插入
                er = AddCharIndexOf(er, begin, re.charAt(begin));
                f(re, er, begin + 1, change + 1);
                //System.out.println("插入之后：" + er);
                er = tmp;// 回溯
 
                // 替换
                er = ReplaceCharIndexOf(er, begin, re.charAt(begin));
                f(re, er, begin + 1, change + 1);
                // System.out.println("替换之后：" + er);
                er = tmp;// 回溯
            } else {
                // 如果对应的字符正确，跳过即可
                f(re, er, begin + 1, change);
            }
        }
 
    }
 
    private static String ReplaceCharIndexOf(String er, int begin, char charAt) {
 
        if (begin != er.length() - 1) {
            // 不是结尾的字符串
            er = er.substring(0, begin) + charAt + er.substring(begin + 1);
        } else {
            er = er.substring(0, begin) + charAt;
        }
        return er;
    }
 
    private static String AddCharIndexOf(String er, int begin, char charAt) {
        if (begin == er.length()) {
            // 长度不够 对尾加上即可
            return er + charAt;
        } else {
            return er.substring(0, begin) + charAt + er.substring(begin);
        }
 
    }
 
    private static String RemoveCharIndexOf(String er, int begin) {
 
        if (begin != er.length() - 1) {
            // 不是结尾的字符串
            er = er.substring(0, begin) + er.substring(begin + 1);
        } else {
            er = er.substring(0, begin);
        }
        return er;
    }
 
}