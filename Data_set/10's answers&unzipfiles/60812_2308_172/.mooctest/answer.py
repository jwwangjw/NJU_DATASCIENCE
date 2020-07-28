import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
 
public class Main {
 
    static class Node {
        int val;
        Node left;
        Node right;
        Node parent;
 
        Node(int val) {
            this.val = val;
        }
    }
 
    public static HashMap<Integer, Node> hashmap = new HashMap<Integer, Node>();
 
    public static void buildTree(int head, int left, int right) {
        Node node = null;
        if (hashmap.containsKey(head)) {
            node = hashmap.get(head);
        } else {
            node = new Node(head);
            hashmap.put(head, node);
        }
 
        if (left != 0 && hashmap.containsKey(left)) {
            node.left = hashmap.get(left);
        } else if (left == 0) {
            node.left = null;
        } else {
            node.left = new Node(left);
            node.left.parent = node;
            hashmap.put(left, node.left);
        }
 
        if (right != 0 && hashmap.containsKey(right)) {
            node.right = hashmap.get(right);
        } else if (right == 0) {
            node.right = null;
        } else {
            node.right = new Node(right);
            node.right.parent = node;
            hashmap.put(right, node.right);
        }
 
    }
 
    public static Node findNextNode(Node checkNode) {
        if (checkNode.right != null) {
            Node cc = checkNode.right;
            while (cc.left != null) {
                cc = cc.left;
            }
            return cc;
        } else {
            Node p = checkNode;
            while (p.parent != null && p.parent.left != p) {
                p = p.parent;
            }
            return p.parent;
        }
    }
 
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] str1 = in.readLine().split(" ");
        int n = Integer.parseInt(str1[0]);
        int root = Integer.parseInt(str1[1]);
        for (int i = 0; i < n; ++i) {
            String[] str2 = in.readLine().split(" ");
            buildTree(Integer.valueOf(str2[0]), Integer.valueOf(str2[1]), Integer.valueOf(str2[2]));
        }
        int check = Integer.parseInt(in.readLine().trim());
        Node checkNode = hashmap.get(check);
        Node res = findNextNode(checkNode);
        System.out.println(res == null ? 0 : res.val);
    }
}