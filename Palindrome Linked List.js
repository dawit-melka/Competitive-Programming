var isPalindrome = function(head) {
    var arr = [];
    var current = head;
    while(current){
        arr.push(current.val);
        current = current.next;
    }
    var start = 0;
    var end = arr.length-1;
    while(start<end){
        if(arr[start] !== arr[end]) return false;
        start++;
        end--;
    }
    return true;
};
