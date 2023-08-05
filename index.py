def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


# Example usage:
x1, y1 = 1, 0
x2, y2 = 0, 0
x3, y3 = 0, 2

area = triangle_area(x1, y1, x2, y2, x3, y3)
print("Area of the triangle:", area)
