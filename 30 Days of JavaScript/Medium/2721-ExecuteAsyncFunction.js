/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    // return a new promise
    return new Promise((resolve, reject) => {
        let res = []; // array to store resolved values from the input promises
        let pending = functions.length; // counter to track remaining unresolved promises
        
        // iterate over the array of functions
        functions.forEach((fn, i) => {
            // call the function to get a promise and handle its resolution/rejection
            fn().then(value => {
                res[i] = value; // store the resolved value in the correct index
                pending--; // decrement the counter for unresolved promises

                // if all promises are resolved, resolve the main promise with the results array
                if(pending === 0) {
                    resolve(res);
                }
            }).catch(error => {
                // if any promise rejects, reject the main promise with the encountered error
                reject(error);
            });
        });
    });
};
/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */