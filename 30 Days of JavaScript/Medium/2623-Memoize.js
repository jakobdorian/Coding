/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    // cache object to store computed results for faster retrieval.
    const cache = {};

    // return a new function that takes any number of arguments ('...args').
    return function(...args) {
        // generate a unique key based on the arguments passed to the function using JSON.stringify().
        const key = JSON.stringify(args);
        
        // check if the key already exists in the cache.
        if(key in cache) {
            // if the key exists, return the cached result.
            return cache[key];
        }

        // if the key doesn't exist, compute the result by calling the original function 'fn' with the arguments,
        // store the result in the cache with the key, and return the result.
        return cache[key] = fn(...args);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */