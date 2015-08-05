void LevelOrder(Node root){
    Queue<Node> q = new LinkedList<Node>();
    q.add(root);
    while(q.peek() != null){
        Node node = q.remove();
        System.out.print(node.data+" ");
        if (node.left != null)
            q.add(node.left);
        if (node.right != null)
            q.add(node.right);
    }
}

