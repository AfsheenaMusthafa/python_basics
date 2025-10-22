def rectangle_calculator():
    print("Rectangle Calculator")
    
    length = float(input("Length: "))
    width = float(input("Width: "))

    perimeter = 2 * (length + width)
    area = length * width

    print(f"Perimeter: {perimeter:.0f}")
    print(f"Area: {area:.0f}")

# Call the function
rectangle_calculator()
