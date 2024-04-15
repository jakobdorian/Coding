class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Form pairs of elements from nums1 and nums2
        pairs = [(n1, n2) for n1, n2, in zip(nums1, nums2)]
        # Sort pairs based on the second element of each pair in descending order
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        # Initialize a min-heap to keep track of elements from nums1
        minHeap = []
        # Initialize the sum of elements from nums1
        n1_sum = 0
        # Initialize the maximum score
        res = 0

        # Iterate over sorted pairs
        for n1, n2 in pairs:
            # Add current nums1 element to the sum
            n1_sum += n1
            # Push the current nums1 element to the min-heap
            heapq.heappush(minHeap, n1)

            # If the size of the min-heap exceeds k
            if len(minHeap) > k:
                # Pop the smallest element from the min-heap
                n1_pop = heapq.heappop(minHeap)
                # Subtract the popped element from the sum
                n1_sum -= n1_pop
            # If the size of the min-heap reaches k
            if len(minHeap) == k:
                # Update the maximum score if necessary
                res = max(res, n1_sum * n2)

        # Return the maximum score found
        return res
