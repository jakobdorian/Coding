class TimeLimitedCache {
    // initialize the cache as a Map to store key-value pairs along with their timeout IDs.
    cache = new Map()

    /**
     * sets a value in the cache with a specific duration.
     * @param {any} key - The key to store the value under.
     * @param {any} value - The value to store.
     * @param {number} duration - The duration (in milliseconds) for which the value should be kept in the cache.
     * @returns {boolean} - Returns true if the key already existed in the cache, false otherwise.
     */
    set(key, value, duration) {
        // check if the key already exists in the cache.
        const exists = this.cache.get(key);
        if (exists) {
            // if the key exists, clear the previous timeout to reset the duration.
            clearTimeout(exists.timeoutId);
        }
        // set a timeout to remove the key from the cache after the specified duration.
        const timeoutId = setTimeout(() => {
            this.cache.delete(key);
        }, duration);
        // store the value along with the timeout ID in the cache.
        this.cache.set(key, { value, timeoutId });
        // return true if the key existed, false otherwise.
        return Boolean(exists);
    };

    /**
     * retrieves a value from the cache.
     * @param {any} key - The key whose value needs to be retrieved.
     * @returns {any} - Returns the value if found, otherwise returns -1.
     */
    get(key) {
        // check if the key exists in the cache.
        if (this.cache.has(key)) {
            // return the value associated with the key.
            return this.cache.get(key).value;
        }
        // if the key does not exist, return -1.
        return -1;
    };

    /**
     * counts the number of items currently in the cache.
     * @returns {number} - The number of key-value pairs in the cache.
     */
    count() {
        // return the size of the cache.
        return this.cache.size;
    };
}
