class StockSpanner:
    """
    901. Online Stock Span
    https://leetcode.com/problems/online-stock-span/
    """
    def __init__(self):    
        # we use the stack to keep track the latest price
        self.stack = []

    def next(self, price: int) -> int:
        con = 1
        # as long as the current is greater than the last price, we add a consecutive day
        while len(self.stack) and self.stack[-1][0] <= price:
            # we remove the last price because we counted the consecutive day
            # and other future prices will either reference the current consecutive
            # or they are not big enough
            con += self.stack.pop()[1]
        self.stack.append([price, con])
    
        return con


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)