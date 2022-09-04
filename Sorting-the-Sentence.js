/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let arr= s.split(' ');
   
    for(var i=arr.length; i>0; i--){
       
        for(var j=0; j<i-1; j++){
            if(arr[j].charAt(arr[j].length-1) > arr[j+1].charAt(arr[j+1].length-1)){
                let temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;  
            }
        }
        arr[i-1]=arr[i-1].slice(0,-1)
    }
    
    s=arr.join(" ");
    
    
    return (s);
    
    
};
