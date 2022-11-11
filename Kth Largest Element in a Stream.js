var KthLargest = function(k, nums) {
    this.data = [];
    
    this.k = function (){ return k };
    for (let i = 0; i < nums.length; i++){
        this.add(nums[i]);
    }
    
};

KthLargest.prototype.add = function(val) {
    this.data[this.data.length] = val;
    this.heapifyUp();
    
    if (this.data.length > this.k()) {
        this.poll();
    }
    if (this.data.length === this.k()){
        return this.data[0];
    }
};

KthLargest.prototype.poll = function() {
    this.data[0] = this.data[this.data.length-1];
    this.data.length--;
    this.heapifyDown()
};

KthLargest.prototype.heapifyUp = function() {
    let currentIndex = this.data.length - 1;
    
    while (this.data[currentIndex] < this.data[this.parentIndex(currentIndex)]){
        this.swap (currentIndex, this.parentIndex(currentIndex));
        currentIndex = this.parentIndex(currentIndex);
    }
};

KthLargest.prototype.heapifyDown = function() {
    let currentIndex = 0;
    
    while (this.data[currentIndex] > this.data[this.leftChildIndex(currentIndex)]
          || this.data[currentIndex] > this.data[this.rightChildIndex(currentIndex)]){
        let smallerChildIndex = this.leftChildIndex(currentIndex);
        
        if (this.data[smallerChildIndex] > this.data[this.rightChildIndex(currentIndex)]){
            smallerChildIndex = this.rightChildIndex(currentIndex);
        }
        
        this.swap (currentIndex, smallerChildIndex);
        currentIndex = smallerChildIndex;
    }
};

KthLargest.prototype.swap = function(i1, i2) {
    let temp = this.data[i1];
    this.data[i1] = this.data[i2];
    this.data[i2] = temp;
};

KthLargest.prototype.parentIndex = function(i) {
    return Math.floor((i-1)/2)
};

KthLargest.prototype.leftChildIndex = function(i) {
    return i*2 + 1;
};

KthLargest.prototype.rightChildIndex = function(i) {
    return i*2 + 2;
};
