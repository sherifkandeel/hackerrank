static Node Insert(Node root, int value){
    if (root == null){
        Node temp = new Node();
        temp.data = value;
        temp.left = null;
        temp.right = null;
        return temp;
    }
    else if (root.data < value){
        root.right = Insert(root.right, value);
    }
    else if (root.data > value){
        root.left = Insert(root.left, value);
    }
    return root;
}
