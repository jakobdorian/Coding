class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
    
        # sort the list of products alphabetically
        products.sort()

        # iterate through each character in the search word along with its index
        for i, ch in enumerate(searchWord):
            temp = []
            for p in products:
                # check if the current character matches the character at the same index in the product
                if i < len(p) and ch == p[i]:
                    temp.append(p)
            # append the first three suggestions from the temporary list to the result 
            res.append(temp[:3])
            # update the products list to contain only the suggestions matching the current prefix
            products = temp  
        return res 
