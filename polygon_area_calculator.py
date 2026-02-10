class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        """Set the width of the rectangle"""
        self.width = width
    
    def set_height(self, height):
        """Set the height of the rectangle"""
        self.height = height
    
    def get_area(self):
        """Return the area (width * height)"""
        return self.width * self.height
    
    def get_perimeter(self):
        """Return the perimeter (2 * width + 2 * height)"""
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        """Return the diagonal ((width ** 2 + height ** 2) ** 0.5)"""
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        """Return a string representation of the rectangle using '*' characters"""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        lines = []
        for _ in range(self.height):
            lines.append("*" * self.width)
        
        return "\n".join(lines) + "\n"
    
    def get_amount_inside(self, shape):
        """Return how many times the shape can fit inside this rectangle"""
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        
        return horizontal_fit * vertical_fit
    
    def __str__(self):
        """Return string representation of the rectangle"""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        """Initialize a square with equal width and height"""
        super().__init__(side, side)
        self.side = side
    
    def set_side(self, side):
        """Set the side length (updates both width and height)"""
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, width):
        """Set the width (also sets height for square)"""
        self.set_side(width)
    
    def set_height(self, height):
        """Set the height (also sets width for square)"""
        self.set_side(height)
    
    def __str__(self):
        """Return string representation of the square"""
        return f"Square(side={self.side})"


if __name__ == "__main__":
    # Quick manual tests
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
