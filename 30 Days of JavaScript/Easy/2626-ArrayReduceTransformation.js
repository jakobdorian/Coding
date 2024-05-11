var reduce = function(nums, fn, init) {
    // initialize the result to the initial value.
    let res = init;

    // iterate through each number in the array.
    for(const n of nums) {
        // update the result by applying the reduction function to the current result and the current number.
        res = fn(res, n);
    }

    // using the built-in reduce method to achieve the same result as the loop.
    return nums.reduce(fn, init);
};