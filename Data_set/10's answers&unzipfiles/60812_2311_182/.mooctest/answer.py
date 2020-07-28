import java.io.BufferedReader;
import java.io.InputStreamReader;
 
// //   2019 校招网易：满二叉树转求和树
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        String s1[] = br.readLine().split(" ");
 
        int before[] = new int[s.length];
        int middle[] = new int[s1.length];
 
        for (int i = 0; i < s.length; i++) {
            before[i] = Integer.parseInt(s[i]);
        }
 
        for (int i = 0; i < s1.length; i++) {
            middle[i] = Integer.parseInt(s1[i]);
        }
        int res[] = new int[before.length];  //
        boolean b[] = new boolean[before.length];
        for (int i = 0; i < before.length; i++) {
            fun(before[i],middle,res,b);
        }
        for (int re : res) {
            System.out.print(re + " ");
        }
    }
 
    static void   fun(int tar,int middle[],int res[],boolean b[]){
        int index = -1;
        for (int i = 0; i < middle.length; i++) {
            if (middle[i] == tar) {
                index = i;
                b[index] = true;
                break;
            }
        }
        if (index == -1)
            return;
        int left = 0,right = 0;
        for (int i = 0;i < index;i++){
            if (b[i])
                continue;
            left += middle[i];
 
        }
        for (int i = index + 1;i < middle.length;i++){
            if (b[i])
                break;
            right += middle[i];
        }
        res[index] = left + right;
    }
 
}