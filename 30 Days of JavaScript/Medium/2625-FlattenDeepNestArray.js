var flat = function (arr, n) {
    // an empty array 'res' to store the flattened result
    const res = [];
    
    function helper(arr, depth) {
        // iterate over each element in the array
        for (const val of arr) {
            // if the element is an object (array) and the current depth is less than 'n'
            if (typeof val === 'object' && depth < n) {
                // recursively call the helper function, increasing the depth by 1
                helper(val, depth + 1);
            } else {
                // otherwise, push the element to the result array
                res.push(val);
            }
        }
        // return the result array
        return res;
    }
    // start the helper function with the initial array and depth 0
    return helper(arr, 0);
};
