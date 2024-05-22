/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    // declare a variable to store the timeout ID.
    let id;
    
    // return a new function that will be the debounced version of the original function (fn).
    return function(...args) {
        // clear any existing timeout to reset the debounce period.
        clearTimeout(id);
        
        // set a new timeout to invoke the function (fn) after the specified wait time (t).
        // the function (fn) will receive all the arguments (...args) passed to the debounced function.
        id = setTimeout(() => fn(...args), t);
    };
};
/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */