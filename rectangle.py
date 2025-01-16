class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        # First yield length
        yield {'length': self.length}
        # Then yield width
        yield {'width': self.width}

# Example usage
def test_rectangle():
    # Create a rectangle with length 5 and width 3
    rect = Rectangle(5, 3)
    
    # Iterate over the rectangle
    for dimension in rect:
        print(dimension)

if __name__ == "__main__":
    test_rectangle()