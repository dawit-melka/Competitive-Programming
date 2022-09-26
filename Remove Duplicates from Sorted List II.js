var deleteDuplicates = function(head) {
    var current = head;
    var prev = head;
   
    while(current){
        if(!current.next) break;
        if(current.val === current.next.val){
            if(current === head){
                while(current.val === current.next.val){
                    current = current.next;
                    if(!current.next) return null;
                } 
                head = current.next;
            }else{
                while(current.val === current.next.val){
                    current = current.next;
                    if(!current.next) break;
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
