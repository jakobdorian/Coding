/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        var res = x
        // iterate through the array of functions in reverse order
        for (var i = functions.length - 1; i >=0; i--) {
            // call each function in the array with the current value of 'res'
            // and update 'res' with the result
            res = functions[i](res)
        }
        // return the final result after applying all the functions
        return res;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
 