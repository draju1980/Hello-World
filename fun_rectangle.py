#Write a function that accepts two positive integers which are the height and width of a rectangle
#and returns a list that contains the area and perimeter of that rectangle.
def cal_reactangle(height,width):
    rectangle_area=height*width
    rectagnle_perimeter=2*(height+width)
    return [rectangle_area,rectagnle_perimeter]
