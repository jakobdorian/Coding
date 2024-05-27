/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    // an empty object to hold the grouped elements
    var m = {};

    // iterate over each element in the array
    for (var i = 0; i < this.length; i++) {
        // apply the provided function to the current element to determine the key
        var key = fn(this[i]);

        // if the key does not exist in the object, create an empty array for this key
        if (!(key in m)) {
            m[key] = [];
        }

        // add the current element to the array associated with the key
        m[key].push(this[i]);
    }

    // return the object containing the grouped elements
    return m;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */