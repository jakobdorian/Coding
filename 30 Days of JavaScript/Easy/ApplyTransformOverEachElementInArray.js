/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // easy method, no state, no variables
    // return arr.map(fn);
    
    // loop method
    // dynamic array
    const res = new Array(arr.length);
    for (const i in arr) {
        res[i] = (fn(arr[i], Number(i)));
    }
    return res;
};