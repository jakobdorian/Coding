# Enter your code here. Read input from STDIN. Print output to STDOUT

class QueueTwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    # 1
    def enqueue(self, x):
        self.s1.append(x)
    # 2
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
        else:
            return None
    # 3
    def front(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]
        else:
            return None
    
def process_queries(queries):
    q = QueueTwoStacks()
    res = []
        
    for query in queries:
        if query[0] == 1:
            q.enqueue(query[1])
        elif query[0] == 2:
            q.dequeue()
        elif query[0] == 3:
            res.append(q.front())
    return res

# read input
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    queries = []
    for line in data:
        query = list(map(int, line.split()))
        queries.append(query)
        
    res = process_queries(queries)

    for r in res:
        print(r)