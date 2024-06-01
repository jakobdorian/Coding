class EventEmitter {
    eventMap = {}; // an object to store event names and their corresponding sets of callback functions.

    /**
     * Subscribes a callback function to a specific event.
     * @param {string} eventName - The name of the event to subscribe to.
     * @param {Function} callback - The callback function to execute when the event is emitted.
     * @return {Object} - An object with an unsubscribe method to remove the callback from the event.
     */
    subscribe(eventName, callback) {
        // check if the event name is already in the eventMap, if not, create a new set for it.
        if (!this.eventMap.hasOwnProperty(eventName)) {
            this.eventMap[eventName] = new Set();
        }
        // add the callback function to the set of the specified event.
        this.eventMap[eventName].add(callback);

        // return an object with an unsubscribe method to remove the callback from the event.
        return {
            unsubscribe: () => {
                this.eventMap[eventName].delete(callback);
            }
        };
    }

    /**
     * Emits an event, invoking all subscribed callback functions with the provided arguments.
     * @param {string} eventName - The name of the event to emit.
     * @param {Array} args - An array of arguments to pass to the callback functions.
     * @return {Array} - An array of results from the callback functions.
     */
    emit(eventName, args = []) {
        const res = []; // array to store the results of the callback functions.

        // iterate over the set of callback functions for the event and invoke each with the provided arguments.
        (this.eventMap[eventName] ?? []).forEach((callback) => res.push(callback(...args)));

        // return the array of results.
        return res;
    }
}


/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */