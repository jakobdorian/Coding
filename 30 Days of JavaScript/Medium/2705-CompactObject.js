/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj
            // remove falsy values
            .filter(value => Boolean(value))
            // recursively compact nested objects/arrays
            .map(value => (typeof value === 'object' && value !== null ? compactObject(value) : value)); 
  } else if (obj !== null && typeof obj === 'object') {
    const compacted = {};
    for (const [key, value] of Object.entries(obj)) {
      // only include truthy values
      if (Boolean(value)) {
        // recursively compact nested objects/arrays
        compacted[key] = typeof value === 'object' ? compactObject(value) : value;
      }
    }
    return compacted;
  }
  return obj; // if it's not an object or array, return it as is
};
