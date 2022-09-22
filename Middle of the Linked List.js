var middleNode = function(head) {
    let length = 0;
    let current = head;
    while(current !== null){
        current = current.next;
        length++;
    }
    let half = Math.floor(length/2);
    current = head;
    for(let i = 0; i<half; i++){
        current = current.next;
    }
    
    return current
};
