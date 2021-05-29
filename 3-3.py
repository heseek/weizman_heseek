# def myfuc(a, b, type='+', repeat=1):
#     result = 0
#     for i in range(repeat):
#         if type == '+':
#             result += a + b
class Clac:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a+self.b
        return self.a + self.b
