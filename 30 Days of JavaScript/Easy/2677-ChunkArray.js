/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const res = [];
    let sub = [];
    
    // loop through each element in the input array.
    for (let i = 0; i < arr.length; i++) {
        // add the current element to the current chunk.
        sub.push(arr[i]);
        
        // if the current chunk has reached the specified size,
        // add it to the result array and reset the chunk.
        if (sub.length === size) {
            res.push(sub);
            sub = [];
        }
    }
    
    // after the loop, if there are any remaining elements in the current chunk,
    // add them as a final chunk to the result array.
    if (sub.length) {
        res.push(sub);
    }
    
    // return the result array containing all chunks.
    return res;
};
