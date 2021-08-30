class Rectangle:

  def __init__(self, width, height):
    self.width = width 
    self.height = height 

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * (self.width + self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal

  def get_picture(self):
    picture = ''
    
    if self.width > 50 or self.height > 50:
        picture += "Too big for picture."
    else:
        for i in range(self.height):
          picture += '*' * self.width
          picture += '\n'
      
    return picture

  def get_amount_inside(self, shape):
      
      if shape.width > self.width or shape.height > self.height:
          return 0
      else:
        return (self.width // shape.width) * (self.height // shape.height)
  
  def __str__(self):
      return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = self.height = side 
        
    def set_side(self, new_side):
        self.width = self.height = new_side
        
    def __str__(self):
        return f"Square(side={self.width})"
        
        
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
    
    
    