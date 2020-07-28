import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
 
class TreeNode {
    int path;    // 共用此节点的单词数
    int end;     // 以此节点为结尾的单词数
    TreeNode[] map;  // 哈希表 key为某一条字符路径，value为字符路径指向的节点
    public TreeNode() {
        path = 0;
        end = 0;
        map = new TreeNode[26]; // 小写字母26个
    }
}
 
public class Main {
     
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.valueOf(in.readLine());
        Trie trie = new Trie();
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String[] lineArr = in.readLine().split(" ");
            int op = Integer.valueOf(lineArr[0]);
            String word = lineArr[1];
            switch (op) {
                case 1:
                    trie.insert(word);
                    break;
                case 2:
                    trie.delete(word);
                    break;
                case 3:
                    res.append(trie.search(word) ? "YES" : "NO").append('\n');
                    break;
                case 4:
                    res.append(trie.prefixNumber(word)).append('\n');
                    break;
            }
        }
        System.out.println(res.substring(0, res.length() - 1));
    }
}
 
class Trie {
    private static TreeNode root;
     
    public Trie() {
        root = new TreeNode();
    }
     
    public static void insert(String word) {
        if (word == null || word.length() == 0) {
            return;
        }
        char[] chas = word.toCharArray();
        TreeNode node = root;
        node.path++;
        int index = 0;
        for (int i = 0; i < chas.length; i++) {
            index = chas[i] - 'a';    // 当前字符对应的字符路径
            if (node.map[index] == null) {
                node.map[index] = new TreeNode();
            }
            node = node.map[index];
            node.path++;
        }
        node.end++;
    }
     
    public static void delete(String word) {
        if (search(word)) {  // 删除前查找是否存在word
            char[] chas = word.toCharArray();
            TreeNode node = root;
            node.path--;
            int index = 0;
            for (int i = 0; i < chas.length; i++) {
                index = chas[i] - 'a';
                if (--node.map[index].path == 0) {  // 直接断开，即删除后序的所有结点
                    node.map[index] = null;
                    return;
                }
                node = node.map[index];
            }
            node.end--;
        }
    }
     
    public static boolean search(String word) {
        if (word == null || word.length() == 0) {
            return false;
        }
        char[] chas = word.toCharArray();
        TreeNode node = root;
        int index = 0;
        for (int i = 0; i < chas.length; i++) {
            index = chas[i] - 'a';
            if (node.map[index] == null) {
                return false;
            }
            node = node.map[index];
        }
        return node.end != 0;
    }
     
    public static int prefixNumber(String pre) {
        if (pre == null || pre.length() == 0) {
            return 0;
        }
        char[] chpre = pre.toCharArray();
        TreeNode node = root;
        int index = 0;
        for (int i = 0; i < chpre.length; i++) {
            index = chpre[i] - 'a';
            if (node.map[index] == null) {
                return 0;
            }
            node = node.map[index];
        }
        return node.path;
    }
}