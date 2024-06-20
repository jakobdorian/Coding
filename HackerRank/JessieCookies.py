import heapq

def cookies(k, A):
    # init min heap
    heapq.heapify(A)
    operations = 0
    # combine the two least cookies
    while A[0] < k and len(A) > 1:
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)
        
        new_cookie = least_sweet + 2 * second_least_sweet
        heapq.heappush(A, new_cookie)
        operations += 1
    # check i fthe min sweetness meets the requirements
    if A[0] >= k:
        return operations
    else:
        return -1
    