import java.util.Scanner;
public class Main {
    static String s1;//用于保存展开后的字符串
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int p1 = scanner.nextInt();
        int p2 = scanner.nextInt();
        int p3 = scanner.nextInt();
        String s = scanner.next();
        s1 = "";//初始化
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '-') {
                if (i == 0 || i == s.length() - 1) { //去掉以'-'开头和结尾的情况
                    s1 = s1 + c;//不符合情况时，将'-'加到字符串中
                    continue;
                }
//获取'-'前后的字符
                char c1 = s.charAt(i - 1);
                char c2 = s.charAt(i + 1);
//前面比后面大时，不修改
                if (c1 >= c2) {
                    s1 = s1 + c;
                } else if (c2 - c1 == 1)//相差为1时，去掉'-'
                    continue;
                else {//判断前后字符是否属于同一类型
                    if (c1 >= 48 && c1 <= 57 && c2 >= 48 && c2 <= 57)//都为数字
                        P(c1, c2, p1, p2, p3);
                    else if (c1 >= 65 && c1 <= 90 && c2 >= 65 && c2 <= 90)//都为打字字母
                        P(c1, c2, p1, p2, p3);
                    else if (c1 >= 97 && c1 <= 122 && c2 >= 97 && c2 <= 122)//都为小写字母
                        P(c1, c2, p1, p2, p3);
                    else {//不为同一类型
                        s1 = s1 + c;
                    }
                }
            } else {
//当前不是'-'时，直接加入
                s1 += c;
            }
        }
        System.out.println(s1);
    }
    private static void P(char c1, char c2, int p1, int p2, int p3) {
    //处理不包括边界，
        int c = c1 + 1;
        int end = c2 + 0;
        String ss = "";
        for (int i = c; i < end; i++) {
            char l = (char) i;//将数字转换成对应的字符
            for (int j = 1; j <= p2; j++) {//根据p2循环加次数
                if (p1 != 3)
                    ss += l;
                else {//根据p3变成'*'
                    ss += '*';
                }
            }
        }
        if (p1 == 1)
            ss = ss.toLowerCase();//转换小写
        else if (p1 == 2)
            ss = ss.toUpperCase();//转换大写
        if (p3 == 2)
            ss = new StringBuffer(ss).reverse().toString();//反转
        s1 = s1 + ss;
    }
}