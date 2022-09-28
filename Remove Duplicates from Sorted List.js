var deleteDuplicates = function(head) {

    var current = head;
    var delay = head;
    while(current){
        if(current.val !== delay.val){
            delay.next = current;
            delay = current
        }
        if(delay.val === current.val & !current.next) delay.next = null;
        current = current.next;
    }
    return head
};
