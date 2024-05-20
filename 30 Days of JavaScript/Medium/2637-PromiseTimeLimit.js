/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise(async (resolve, reject) => {
            const id = setTimeout(() => reject("Time Limit Exceeded"), t)
            // attempt to execute the original function
            try {
                const res = await fn(...args);
                resolve(res);
            } catch(err) {
                reject(err);
            } finally {
                clearTimeout(id);
            }
            
        })
    }
};
