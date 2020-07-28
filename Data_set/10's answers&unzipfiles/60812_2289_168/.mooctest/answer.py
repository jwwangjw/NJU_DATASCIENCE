import java.util.*;
 
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = scanner.nextInt();
        }
        System.out.println(isPostOrder(arr, 0, n-1));
         
    }
     
     
    private static boolean isPostOrder(int arr[],int start,int end) {
        if(start >=end) return true;
         
        int rootVal = arr[end];
        boolean flag = false;
        int mid = end;
        for(int i=start;i<end;i++) {
            if(!flag && arr[i]>rootVal) {
                mid = i;
                flag = true;
            }else if(flag && arr[i]<rootVal) {
                return false;
            }
        }
         
        return isPostOrder(arr, start, mid-1) && isPostOrder(arr, mid, end-1);
    }
}