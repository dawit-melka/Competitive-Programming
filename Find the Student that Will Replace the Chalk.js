var chalkReplacer = function(chalk, k) {
    if(chalk[0] > k || chalk.length ===1) return 0;
    
    for(var i=1; i < chalk.length; i++){ 
        chalk[i] = chalk[i-1] + chalk[i];
        if(chalk[i] > k) return i;  
    }
    
    var left = k % chalk[chalk.length-1];
        
    for(var i=0; i < chalk.length; i++){
        var temp = left - chalk[i];
        if(temp < 0){
            return i;
        }
    }
};
