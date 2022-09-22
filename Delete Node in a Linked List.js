var deleteNode = function(node) {
    let current = node;
    while(current != null){
        current.val = current.next.val;
        
        if(current.next.next == null){
            current.next = null
            this.length--;
            break;
        }
        current = current.next;
    }
};
