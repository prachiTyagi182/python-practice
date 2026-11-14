def area(length, width=None, shape='rectangle'):
    if shape == 'square':
        return length * length
    else: # rectangle
        if width is None:
            width = length # Agar width na di ho toh length ko hi width maan lein
        return length * width



rect_area = area(10, 5)
print("Rectangle Area (Positional):", rect_area)


square_area = area(4, shape='square')
print("Square Area (Default style):", square_area)


custom_area = area(length=8, width=3, shape='rectangle')
print("Rectangle Area (Keyword style):", custom_area)