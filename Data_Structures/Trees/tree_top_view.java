void top_view(Node root){
    print_left(root.left);
    System.out.print(root.data+ " ");
    print_right(root.right);
}

void print_left(Node root){
    if (root == null)
        return;
    print_left(root.left);
    System.out.print(root.data+" ");
}

void print_right(Node root){
    if (root == null)
        return;
    System.out.print(root.data+" ");
    print_right(root.right);
}
