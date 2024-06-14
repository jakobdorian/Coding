class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if the total number of cards is not a multiple of groupSize, we cannot split them into groups of groupSize
        if len(hand) % groupSize:
            return False
        
        # dictionary to count occurrences of each card
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # create a min-heap with the unique card values
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        # while there are cards in the heap
        while minHeap:
            # get the smallest card number
            first = minHeap[0]
            
            # check if we can form a consecutive sequence starting with 'first'
            for i in range(first, first + groupSize):
                if i not in count:  # if the card 'i' is not in the count dictionary
                    return False
                count[i] -= 1  # use one occurrence of card 'i'
                if count[i] == 0:  # if no more occurrences of card 'i'
                    if i != minHeap[0]:  # check if the current card 'i' is at the top of the heap
                        return False
                    heapq.heappop(minHeap)  # remove the card from the heap
        return True
        