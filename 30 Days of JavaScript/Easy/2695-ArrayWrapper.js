var ArrayWrapper = function(nums) {
    // initialize the nums property with the given array
    this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function() {
    // Reduce the nums array to its sum and return the result
    return this.nums.reduce(
        (n, a) => n + a , 0
    );
}

ArrayWrapper.prototype.toString = function() {
    // Convert the nums array to a string and format it as "[element1,element2,...]"
    return `[${String(this.nums)}]`;
}
