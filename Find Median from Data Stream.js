var MedianFinder = function() {
    this.maxHeap = [];
    this.minHeap = [];
};

// Keep the min and max heap size balanced (at max differ by 1)
//maxHeap holds the left (smaller) values
//minHeap holds the right (larger) values
// maxHeap[0] <= minHeap[0]
MedianFinder.prototype.addNum = function(num) {
    this.maxHeap.push(num);
    this.bubbleUpMaxHeap();

    if (this.maxHeap.length - this.minHeap.length > 1) {
        this.minHeap.push (this.pollMaxHeap());
        this.bubbleUpMinHeap()
    }

    if (this.maxHeap[0] > this.minHeap[0]) {
        this.minHeap.push (this.pollMaxHeap());
        this.bubbleUpMinHeap()
    }

    if (this.minHeap.length - this.maxHeap.length > 1) {
        this.maxHeap.push (this.pollMinHeap())
        this.bubbleUpMaxHeap() 
    }
};


MedianFinder.prototype.findMedian = function() {
// if both heaps have equal size return the average of the min and max values
    if (this.maxHeap.length === this.minHeap.length) {
        return (this.maxHeap[0] + this.minHeap[0]) / 2;
    }
    return this.maxHeap.length > this.minHeap.length ? this.maxHeap[0] : this.minHeap[0];
};

MedianFinder.prototype.pollMaxHeap = function() {
    let maxValue = this.maxHeap[0];
    this.maxHeap[0] = this.maxHeap.at(-1);
    this.maxHeap.pop();
    this.sinkDownMaxHeap();
    return maxValue;
}

MedianFinder.prototype.pollMinHeap = function() {
    let minValue = this.minHeap[0];
    this.minHeap[0] = this.minHeap.at(-1);
    this.minHeap.pop();
    this.sinkDownMinHeap();
    return minValue;
}


MedianFinder.prototype.bubbleUpMaxHeap = function() {
    let index = this.maxHeap.length - 1;
    
    while (this.maxHeap[index] > this.maxHeap[Math.floor((index - 1) / 2)]) {
        this.swap (index, Math.floor((index - 1) / 2), this.maxHeap);
        index = Math.floor((index - 1) / 2);
    }
};

MedianFinder.prototype.bubbleUpMinHeap = function() {
    let index = this.minHeap.length - 1;
    
    while (this.minHeap[index] < this.minHeap[Math.floor((index - 1) / 2)]) {
        this.swap (index, Math.floor((index - 1) / 2), this.minHeap);
        index = Math.floor((index - 1) / 2);
    }
};

MedianFinder.prototype.sinkDownMaxHeap = function() {
    let index = 0;
    
    while (this.maxHeap[index] < this.maxHeap[index*2 + 1]
          || this.maxHeap[index] < this.maxHeap[index*2 + 2]) {
        let maxChildIndex = index*2 + 1;
        if (this.maxHeap[maxChildIndex] < this.maxHeap[index*2 + 2]) {
            maxChildIndex = index*2 + 2;
        }
        
        this.swap (index, maxChildIndex, this.maxHeap);
        index = maxChildIndex;
    }
}

MedianFinder.prototype.sinkDownMinHeap = function () {
    let index = 0;
    
    while (this.minHeap[index] > this.minHeap[index*2 + 1]
          || this.minHeap[index] > this.minHeap[index*2 + 2]) {
        let minChildIndex = index*2 + 1;
        if (this.minHeap[minChildIndex] > this.minHeap[index*2 + 2]) {
            minChildIndex = index*2 + 2;
        }
        
        this.swap (index, minChildIndex, this.minHeap);
        index = minChildIndex;
    }
}

MedianFinder.prototype.swap = function (i1, i2, arr) {
    let temp = arr[i1];
    arr[i1] = arr[i2];
    arr[i2] = temp;
}
