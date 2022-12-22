/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    let res = "";
    
    for (let i = 0; i < s.length; i++) {
        if (s[i+2] !== "#"){
            res += String.fromCharCode(parseInt(s[i]) + "a".charCodeAt() - 1)
        }else {
            res += String.fromCharCode(parseInt(s.substring(i, i+2)) + "a".charCodeAt() - 1)
            i += 2;
        } 
    }
    return res;
};