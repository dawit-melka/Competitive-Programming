var mergeTwoLists = function(list1, list2) {
    if(!list1) return list2;
    if(!list2) return list1;
    if(list1.val < list2.val){
        var head = list1;
        list1 = list1.next;
    }else{
        var head = list2;
        list2 = list2.next;
    }
    var current = head;
    while(list1 || list2){
        if(!list1){
            current.next = list2; 
            break;
        } 
        if(!list2){
            current.next = list1; 
            break;
        } 
        if(list1.val < list2.val){
        current.next = list1;
        list1 = list1.next
        }else{
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    return head;
};
