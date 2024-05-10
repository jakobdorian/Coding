var filter = function(arr, fn) {
    var res = [];
    var L = arr.length;
    // iterate through each element of the array using a for loop
    for (var i = 0; i < L; i++) {
        // check if the function 'fn' returns true for the current element
        if(fn(arr[i], i)) {
            // If 'fn' returns true, push the current element to the result array
            res.push(arr[i]);
        }
    }
    // return the resulting array containing filtered elements
    return res;
};
