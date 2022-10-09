var corpFlightBookings = function(bookings, n) {
    var ans = Array(n).fill(0);
    for(var b of bookings){
        ans[b[0]-1]+=b[2];
        if(b[1] !== n) ans[b[1]] -= b[2];
    }
    for(var i=1; i<ans.length; i++){
        ans[i] = ans[i]+ans[i-1];
    }

    return ans
};
