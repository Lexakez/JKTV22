class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def rectS(self):
        return self.a * self.b

    def rectP(self):
        return 2 * (self.a + self.b)
    
    def info(self):
        print(f"Rectangle {self.a} x {self.b} S = {self.rectS()} P = {self.rectP()}")