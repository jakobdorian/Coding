/**
 * @param {Object|Array} obj
 * @return {boolean}
 */

var isEmpty = function(obj) {
    // C`check if the type of obj is 'object'
    if (typeof(obj) == 'object') {
        // if obj is an object, check if it has no own enumerable properties
        // return true if the object has no properties, otherwise return false
        return Object.keys(obj).length === 0;
    } else {
        // if obj is not an object (e.g., string, array), check if its length is 0
        // return true if the length is 0, otherwise return false
        return obj.length === 0;
    }
};