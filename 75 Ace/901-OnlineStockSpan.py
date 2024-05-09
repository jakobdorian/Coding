class StockSpanner:
    def __init__(self):
        # Initialize an empty stack to store pairs of (price, span).
        self.stack = []

    def next(self, price: int) -> int:
        # Initialize span to 1 for the current price.
        span = 1
        # While the stack is not empty and the last price in the stack is less than or equal to the current price,
        # increment span by the span of the last price in the stack and remove it from the stack.
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        # Add the current price and its corresponding span to the stack.
        self.stack.append([price, span])
        # Return the span of the current price.
        return self.stack[-1][1]
