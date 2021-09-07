class rg:
    def __init__(self, start: int, stop:int = '@$^*fhYLu', step: int = '@$^*fhYLu'):
        self.start = start
        self.stop = stop
        self.step = step
        if self.stop == self.step == '@$^*fhYLu':
            self.stop = self.start
            self.start = 0
            self.step = 1
        elif self.step == '@$^*fhYLu':
            self.stop = 1
        n = self.start
        self.range = []
        if self.step == 0:
            raise ValueError
        elif self.step > 0:
            while n < self.stop:
                self.range.append(n)
                n += self.step
        elif self.step < 0:
            while n > self.stop:
                self.range.append(n)
                n += self.step
        # self.range_t = tuple(self.range)

    def __repr__(self) -> tuple:
        return str(tuple(self.range))

# def rg(a: int, b: int = '@$^*fhYLu', c: int = '@$^*fhYLu') -> tuple:
#     """Замена RANGE (tuple)"""
#     if b == c and b == '@$^*fhYLu':
#         b = a
#         a = 0
#         c = 1
#     elif c == '@$^*fhYLu':
#         c = 1
#     list1 = []
#     n = int(a)
#     b = int(b)
#     c = int(c)
#     if c == 0:
#         raise ValueError
#     elif se > 0:
#         while n < b:
#             list1.append(n)
#             n += c
#     elif c < 0:
#         while n > b:
#             list1.append(n)
#             n += c
#     return tuple(list1)
#
# range()
# print(rg(-10, 22, 1))
