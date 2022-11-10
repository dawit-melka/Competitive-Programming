var addTwoNumbers = function(l1, l2) {
    let remainder = 0;
    let head = new ListNode();
    let curr = head;
    
    while (l1 || l2  || remainder) {
        let x = l1 ? l1.val : 0;
        let y = l2 ? l2.val : 0;
        let sum = remainder + x + y;
        remainder = Math.floor(sum/10);
        curr.next = new ListNode(sum % 10);
        
        curr = curr.next;
        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }
    
    return head.next;
};
