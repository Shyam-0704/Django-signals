class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def __iter__(self):
        
        return iter([{'length': self.length}, {'width': self.width}])


result = Rectangle(10, 5)

for values in result:
    print(values)
