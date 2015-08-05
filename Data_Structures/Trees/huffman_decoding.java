void decode(String S, Node root)
{
    String decoded = "";
    Node start = root;
    for (int i=0; i<S.length();i++){
        if (S.charAt(i) == '1')
            start = start.right;
        else if (S.charAt(i) == '0')
            start = start.left;
        if (start.left == null && start.right == null){
            decoded += start.data;
            start = root;
        }
    }
    System.out.print(decoded);

}
