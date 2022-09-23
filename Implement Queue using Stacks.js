var MyQueue = function(){
    this.stack = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.stack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    
    return this.stack.shift()
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    return this.stack[0];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return this.stack.length === 0;
};
