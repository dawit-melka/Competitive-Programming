var middleNode = function(head) {
    
    function traverse(slow, fast) {
        if(!fast || !fast.next) return slow;
        return traverse(slow.next, fast.next.next);
    }
    return traverse(head, head);
};
