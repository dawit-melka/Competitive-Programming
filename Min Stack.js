class Node{
    constructor(val, min){
        this.val = val;
        this.next = null;
        this.min = Math.min(val, min);
    }
}

var MinStack = function() {
    this.first = null;
    this.last = null;
    this.size = 0; 
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    var newNode = new Node(val, this.size === 0 ? Infinity : this.first.min)
    if(this.size === 0){
        this.first = newNode;
        this.last = newNode
    }else{
        newNode.next = this.first;
        this.first = newNode;
    }
    this.size++;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if(!this.first) return null;
    if(this.first === this.last){
        this.last = null;
    }
    this.first = this.first.next;
    
    this.size--;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.first.val;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.first.min;
};
