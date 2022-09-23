class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class MyQueue{
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0
    }
    
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    var newNode = new Node(x);
    if(!this.first){
        this.first = newNode;
        this.last = newNode;
    }else{
        this.last.next = newNode;
        this.last = newNode;
    }
    this.size++;
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    if(!this.first) return null;
    var popped = this.first;
    if(this.size === 1){
        this.last = null;
    }
    this.first = this.first.next;
    this.size--;
    return popped.val;
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    return this.first.val;
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return this.size === 0;
};
