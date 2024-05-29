var join = function(arr1, arr2) {
    const res = {};

    // iterate over the first array
    for(let i = 0; i < arr1.length; i++){
        // use the 'id' property as the key and store the entire object in 'res'
        res[arr1[i].id] = arr1[i];
    }

    // iterate over the second array
    for(let i = 0; i < arr2.length; i++){
        // check if the current object from arr2 already exists in 'res'
        if(res[arr2[i].id]){
            // if it exists, merge the properties from arr2 into the existing object
            for(const key in arr2[i]) {
                res[arr2[i].id][key] = arr2[i][key];
            }
        } else{
            // if it doesn't exist, add the new object from arr2 to 'res'
            res[arr2[i].id] = arr2[i];
        }
    }
    
    // convert the 'res' object back into an array of values and return it
    return Object.values(res);
};
