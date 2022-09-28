var removeNthFromEnd = function(head, n) {
    if(!head.next) return null;
    var current = head;
    var delay = head;
    
    while(current){
        if(n === -1) delay = delay.next;
        else n--;
        current = current.next;
    }
    if(delay === head & n === 0) head = delay.next;
    else delay.next = delay.next.next;
    return head;
};
