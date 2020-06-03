class Cylinder:
  pi=3.14
  def __init__(self,height=1,radius=1):
    self.height=height
    self.radius=radius
   
  def volume(self):
    # print("Height of Cylinder is "+self.height)
    # print("Radius of Cylinder is "+self,radius)
    return Cylinder.pi * self.radius * self.height * self.radius

  def surface_area(self):
    # print("Height of Cylinder is "+self.height)
    # print("Radius of Cylinder is "+self,radius)
    return ((2*Cylinder.pi * self.radius) * self.height) + ((Cylinder.pi * self.radius**2)*2)