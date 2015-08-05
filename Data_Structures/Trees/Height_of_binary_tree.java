int height(Node root){
    if (root == null)
        return 0;
    int left = 1 +  height(root.left);
    int right = 1 + height(root.right);
    return left>right?left:right;
}
