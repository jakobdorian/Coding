/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */

var addTwoPromises = async function(promise1, promise2) {
    // await both promises to resolve concurrently using Promise.all() and store their resolved values in num1 and num2
    const [num1, num2] = await Promise.all([promise1, promise2]);
    // return the sum of num1 and num2
    return num1 + num2; 
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */