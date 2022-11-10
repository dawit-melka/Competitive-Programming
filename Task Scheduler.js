class MaxHeap {
    constructor () {
        this.data = [];
    }
    
    parentIndex (i) {
        return Math.floor((i-1)/2);
    }
    
    leftChildIndex (i) {
        return i*2 + 1;
    }
    
    rightChildIndex (i) {
        return i*2 + 2;
    }
    
    swap (i1, i2) {
        let temp = this.data[i1];
        this.data[i1] = this.data[i2];
        this.data[i2] = temp;
    }
    
    heapifyUp () {
        let currentIndex = this.data.length - 1;
        
        while (this.data[currentIndex] > this.data[this.parentIndex(currentIndex)]) {
            this.swap (currentIndex, this.parentIndex(currentIndex));
            currentIndex = this.parentIndex(currentIndex);
        }
    }
    
    heapifyDown () {
        let currentIndex = 0;
        
        while (this.data[currentIndex] < this.data[this.leftChildIndex(currentIndex)] 
              || this.data[currentIndex] < this.data[this.rightChildIndex(currentIndex)]) {
            let maxChildIndex = this.leftChildIndex(currentIndex);
            
            if (this.data[maxChildIndex] < this.data[this.rightChildIndex(currentIndex)]) {
                maxChildIndex = this.rightChildIndex(currentIndex); 
            }
            
            this.swap(currentIndex, maxChildIndex);
            currentIndex = maxChildIndex;
        }
    }
    
    push (val) {
        this.data[this.data.length] = val;
        this.heapifyUp();
    }
     
    poll () {
        if (this.data.length === 0) return null;
        const maxValue = this.data[0];
        this.data[0] = this.data[this.data.length-1];
        this.data.length--;
        this.heapifyDown();
        return maxValue;
    }
}

var leastInterval = function(tasks, n) {
    const queue = [];
    const heap = new MaxHeap();
    const frequency = {};
    let time = 0;
    
    for (let task of tasks){
        frequency[task] = (frequency[task] || 0) + 1;
    }
    
    for (let key in frequency){
        heap.push(frequency[key]);
    }
    
    while (heap.data.length || queue.length){
        time++;
        if (heap.data.length) {
            let current = heap.poll() - 1;
            if (current) {
                queue.push([current, time + n]);
            }
        }
         
        if (queue.length && queue[0][1] === time) {
            heap.push(queue[0][0]);
            queue.shift();
        }
    }
    return time;
};
