class RecentCounter:
    def __init__(self):
        # a deque to store timestamps and a count to keep track of the number of pings.
        self.q = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        # add the current timestamp to the deque and increment the count of pings.
        self.q.append(t)
        self.count += 1

        # remove timestamps from the beginning of the deque that are older than 3000 milliseconds (3 seconds) and update count
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.count -= 1

        # return the count of pings within the last 3000 milliseconds.
        return self.count
        