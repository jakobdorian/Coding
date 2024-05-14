/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    // flag to track whether the function has been invoked
    var flag = false;
    
    // return a closure that encapsulates the original function
    return function(...args){
        // if the function has already been invoked, return undefined
        if (flag) return undefined;
        
        // set the flag to true to indicate that the function has been invoked
        flag = true;
        
        // execute the original function with the provided arguments and return the result
        return fn(...args);
    }
};
/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
