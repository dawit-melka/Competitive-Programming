var carPooling = function(trips, capacity) {
    var vehicle = [capacity];
    var i = trips[0][1];
    var sum = 0;
    for(var t of trips){
        vehicle[t[1]] =(vehicle[t[1]] || 0) -t[0];
        vehicle[t[2]] =(vehicle[t[2]] || 0) +t[0];
    }
    for(var x of vehicle){
        if(x) sum += x;
        if(sum < 0) return false;
    }
    return true;
};
