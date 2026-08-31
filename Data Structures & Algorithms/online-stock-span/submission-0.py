class StockSpanner:

    def __init__(self):
        self.lst = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.lst and self.lst[-1][0] <= price:
            span += self.lst[-1][1]
            self.lst.pop()
        self.lst.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)