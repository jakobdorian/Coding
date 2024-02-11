class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []  # Store the k smallest pairs found so far. Initialized as an empty list.
        heap = []  # Min-heap to store pairs based on their sum. Initialized as an empty list.
        visited = set()  # Set to keep track of visited indices in nums1 and nums2. Initialized as an empty set.

        # base case
        if not nums1 or not nums2 or not k:  
            return [] 

        # push the first pair (nums1[0], nums2[0]) and its sum to the heap
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))  

        # while there are remaining pairs to be found (k) and heap is not empty
        while k and heap:
            # pop the smallest sum pair and its indices from the heap
            _, i, j = heapq.heappop(heap)  # pop the smallest sum and its corresponding indices.

            # append the pair [nums1[i], nums2[j]] to the result list
            res.append([nums1[i], nums2[j]])  # append the current pair to the result list.

            # check if moving to the next index in nums1 is valid and not visited
            if i+1 < len(nums1) and (i+1, j) not in visited:  # check if the next index in nums1 is valid and not visited
                # push the next pair and its sum to the heap and mark as visited
                heapq.heappush(heap, (nums1[i+1]+nums2[j],i+1,j)) 
                visited.add((i+1,j))  # mark the next index in nums1 as visited.

            # check if moving to the next index in nums2 is valid and not visited
            if j+1 < len(nums2) and (i, j+1) not in visited:  
                # push the next pair and its sum to the heap and mark as visited
                heapq.heappush(heap, (nums1[i]+nums2[j+1],i,j+1))  
                visited.add((i,j+1)) 
            
            # decrement k to track the number of pairs remaining
            k -= 1 
        return res  # return the list of k smallest pairs
