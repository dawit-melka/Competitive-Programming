var numRescueBoats = function(people, limit) {
    people.sort((a,b) => b-a);
    var r = 0
    var l = people.length-1;
    var boat = 0;
    
    while(r <= l){
        if(people[r] + people[l] <= limit) l--;
        r++;
        boat++;
    }
    return boat;
};
