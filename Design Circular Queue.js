var MyCircularQueue = function(k) {
    this.front = -1;
    this.rear = -1;
    this.nums = new Array(k);
};

MyCircularQueue.prototype.enQueue = function(value) {
    if(this.isFull()) return false;
    else if(this.isEmpty()) this.front++;
    this.rear = (this.rear+1) % this.nums.length;
    this.nums[this.rear] = value;
    return true;
};

MyCircularQueue.prototype.deQueue = function() {
    if(this.isEmpty()) return false;
    var temp = this.nums[this.front];
    if(this.front === this.rear){
        this.front = -1;
        this.rear = -1;
    }else{
        this.front = (this.front+1) % this.nums.length;
    }
    return true;
};

MyCircularQueue.prototype.Front = function() {
    if(this.isEmpty()) return -1;
    return this.nums[this.front];
};

MyCircularQueue.prototype.Rear = function() {
    if(this.isEmpty()) return -1;
    return this.nums[this.rear]
};

MyCircularQueue.prototype.isEmpty = function() {
    return this.front === -1;
};

MyCircularQueue.prototype.isFull = function() {
    return (this.rear+1) % this.nums.length === this.front;
};
