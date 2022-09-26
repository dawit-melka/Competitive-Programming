var deleteDuplicates = function(head) {
    var current = head;
    var prev = head;
   
    while(current && current.next !== null){

        if(current.val === current.next.val){
            if(current === head){
                while(current.next !== null && current.val === current.next.val){
                    current = current.next;
                } 
                head = current.next;
            }else{
                while(current.next !== null && current.val === current.next.val){
                    current = current.next;
                } 
                prev.next = current.next;
                current = prev;
            } 
        }else{
            prev = current;
            current = current.next;
        } 
    }
    return head;
};
